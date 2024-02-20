import duckdb
import polars as pl
import os
import yaml
from datetime import datetime
import requests
import json

"""
This script contains the functions used to load data from source to delta lake.

These functions are applicabable across bronze, silver, and gold layers. 

They are called from layer specific etl jobs that exist in their respective layer directories.

"""

"""
ETL Functions
"""

def read_from_local_duck_db(db_path, query):
    db_path = os.path.join(os.getcwd(), db_path)
    conn = duckdb.connect(db_path)
    return conn.execute(query).pl()


def write_to_local_delta(delta_lake_path, layer, table_name,df):
    delta_table_path = validate_local_delta_path(delta_lake_path, layer, table_name)
    if str(type(df)) == "<class 'polars.lazyframe.frame.LazyFrame'>":
        df.collect().write_delta(delta_table_path, mode="overwrite", overwrite_schema=True)
    else: 
        df.write_delta(delta_table_path, mode="overwrite", overwrite_schema=True)

def read_from_local_delta(delta_lake_path, layer, table_name):
    delta_table_path = validate_local_delta_path(delta_lake_path, layer, table_name)
    print(delta_table_path)
    if len(os.listdir(delta_table_path)) == 0:
        raise Exception("Delta table path is empty.")
    else:
        return pl.scan_delta(delta_table_path)

def load_sql_query(query_path):
    query_path = os.path.join(os.getcwd(), *query_path)
    return open(query_path, "r").read()

def transform_polars_df_with_duckdb(query_path):
    query = load_sql_query(query_path)
    return duckdb.sql(query).pl()

def idempotent_append_to_local_delta(delta_lake_path, layer, table_name,df):
    delta_table_path = validate_local_delta_path(delta_lake_path, layer, table_name) 
    if len(os.listdir(delta_table_path)) == 0:
        print("straight overwrite path reached")
        write_to_local_delta(delta_lake_path, layer, table_name,df) 
    else:
        print("append path reached")
        to_append_df = read_from_local_delta(delta_lake_path, layer, table_name)
        appended_df = (
                        pl.concat(
                                 items=[
                                     to_append_df
                                    ,df.lazy()
                                 ]
                                ,how='vertical_relaxed')
                          .unique()
        )
        write_to_local_delta(delta_lake_path, layer, table_name,appended_df)

def write_api_response_to_disk(url:str, write_path_list:list, **kwargs):
    response = requests.get(url, **kwargs)
    data = response.json()
    now = datetime.now()
    file_name = now.strftime('%Y_%m_%d_%H_%M_%s') + '.json'
    write_dir = os.path.join(os.getcwd(), *write_path_list) 
    if os.path.exists(write_dir):
        pass
    else:
        os.mkdir(write_dir)
    write_path = os.path.join(write_dir,file_name) 
    print(write_path)
    with open(write_path, "w+") as file:
        output = json.dumps(data, indent=2)
        file.write(output)




"""
ETL Execution Functions
"""

# Needed for testing execute_etl function
def mock_function(**kwargs):
    return "mock_result"

def execute_etl(to_execute_list: list) -> None:
    results_list = []
    for step in to_execute_list:
        step_description = step['step_description']
        print(f"Attempting execution of '{step_description}'")
        try:
            function_to_execute = step['function_to_execute']
            print(function_to_execute)
            function_to_execute = check_if_allowed(function_to_execute)
            print(function_to_execute)
            function_to_execute_arguments = step['function_to_execute_arguments']
            if "pre_execution_python_code" in step.keys():
                code = step["pre_execution_python_code"] 
                compiled_code = compile(code, "<string>", 'exec')
                print(code)
                exec(compiled_code)
            results = function_to_execute(**function_to_execute_arguments)
            print(results)
            results_list.append(results)
        except Exception as e:
            print(f"Step '{step_description}' failed with the following error:")
            print(str(e))
    print(results_list)
    return results_list

allowed_functions = [
         "read_from_local_duck_db"
        ,"write_to_local_delta"
        ,"transform_polars_df_with_duckdb"
        ,"read_from_local_delta"
        ,"load_sql_query"
        ,"check_missing_values"
        ,"idempotent_append_to_local_delta"
        ,"batch_audit_colum_constraints"
]

def function_not_allowed(**kwargs):
    error_text = "The function passed is not in the allowed function list so this function, `function_not_allowed`, has been substituted instead"
    print(error_text)
    return error_text


def check_if_allowed(function):
    if function in allowed_functions:
        return eval(function)
    else: 
        return function_not_allowed

"""
Data Quality Functions
"""

def check_missing_values(df, table_name):
    return (
                df.null_count()
                  .collect()
                  .transpose(include_header=True)
                  .with_columns(
                         table_name=pl.lit(table_name)
                        ,as_of_datetime=pl.lit(datetime.now())
                      )
                  .rename({
                         "column": "table_column"                     
                        ,"column_0": "null_count"                     
                      })
                  .select(
                        [
                             pl.col("table_name").alias("Table Name")
                            ,pl.col("table_column").alias("Table Column")
                            ,pl.col("null_count").alias("Null Count")
                            ,pl.col("as_of_datetime").alias("As Of Datetime")
                        ]
                      )
    )



def audit_column_constraint(df_name: str, table_name: str, column: str, sql_constraint_predicate: str) -> pl.DataFrame:
    checking_sql = f"SELECT {column} {sql_constraint_predicate} as 'Invalid Record Flag', COUNT(1) as 'Invalid Record Count' FROM {df_name} GROUP BY {column} {sql_constraint_predicate}"
    print(checking_sql)
    audited_df = (
                    duckdb.sql(checking_sql)
                          .pl()
                          .with_columns(
                                 table_name=pl.lit(table_name)
                                ,audit_column=pl.lit(column)
                                ,sql_constraint_predicate=pl.lit(sql_constraint_predicate)
                          )
                          .filter(pl.col("Invalid Record Flag")==True)
                          .select(
                            [
                                 pl.col("table_name").alias("Table Name")
                                ,pl.col("audit_column").alias("Audit Column")
                                ,pl.col("sql_constraint_predicate").alias("SQL Constraint Predicate")
                                ,"Invalid Record Count"   

                            ]
                          )
    )
    return audited_df

def batch_audit_column_constraints(df_name: str, table_name: str, columns_and_predicates_list: list) -> pl.DataFrame:
    as_of_datetime = datetime.now()
    frames = []
    for column_predicate_pair in columns_and_predicates_list:
        column = column_predicate_pair['column']
        sql_constraint_predicate = column_predicate_pair['sql_constraint_predicate']
        frame = audit_column_constraint(df_name, table_name, column, sql_constraint_predicate)
        frames.append(frame)
    finished_frame =  (
        pl.concat(
             items=frames
            ,how='vertical'
            )
          .with_columns(
            as_of_datetime=pl.lit(as_of_datetime)
          )
          .select(
             "Table Name"
            ,"Audit Column"
            ,"SQL Constraint Predicate"
            ,"Invalid Record Count"   
            ,pl.col("as_of_datetime").alias("As Of Datetime")
          )
    )
    return finished_frame

"""
Misc Functions
"""

def validate_local_delta_path(delta_lake_path, layer, table_name):
    delta_lake_path = os.path.join(os.getcwd(),delta_lake_path,layer)
    delta_table_path = os.path.join(delta_lake_path, table_name)
    if os.path.exists(delta_table_path):
        return delta_table_path
    else:
        os.mkdir(delta_table_path)
        return delta_table_path


"""
Main 
"""

def main():
   print("This file is a repository for functions and is not meant to be run. But you ran it anyway and that is okay.") 
if __name__ == "__main__":
    main()

    
