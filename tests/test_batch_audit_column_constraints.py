import pytest
import duckdb
import polars.testing as polars_testing
import polars as pl
from datetime import datetime
from ..src.common.common_data_loading import batch_audit_column_constraints, audit_column_constraint

def test_batch_audit_column_constraints():
    as_of_datetime = datetime.now()
    table_name = "test_table"
    columns = ["id", "name"]
    initial_df = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", None]}).lazy()
    columns_and_predicates_list = [
             {
                 "column": "name"
                ,"sql_constraint_predicate": "IS NULL"
                 }
            ,{
                  "column": "name"
                 ,"sql_constraint_predicate": "= \'Alice\'"
                 }
            ]
    expected_df = pl.DataFrame(
            {
                 "Table Name": [table_name, table_name ] 
                ,"Audit Column" : [ column_predicate_pair["column"] for column_predicate_pair in columns_and_predicates_list]
                ,"SQL Constraint Predicate": [ column_predicate_pair["sql_constraint_predicate"] for column_predicate_pair in columns_and_predicates_list]
                ,"Invalid Record Count" : [1,1]
                } 
           )
   
    actual_df = batch_audit_column_constraints("initial_df", table_name, columns_and_predicates_list)
    

    polars_testing.assert_frame_equal(actual_df.drop("As Of Datetime"), expected_df, check_dtype=False)


if __name__ == "__main__":
    pytest.main()
    
    
