import pytest
import duckdb
import polars.testing as polars_testing
import polars as pl
from datetime import datetime
from ..src.common.common_data_loading import audit_column_constraint

def test_audit_column_constraint():
    as_of_datetime = datetime.now()
    table_name = "test_table"
    columns = ["id", "name"]
    initial_df = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", None]}).lazy()
    column = "name"
    sql_constraint_predicate = "IS NULL"
    expected_df = pl.DataFrame(
            {
                 "Table Name": [table_name] 
                ,"Audit Column" : [column]
                ,"SQL Constraint Predicate": [sql_constraint_predicate]
                ,"Invalid Record Count" : [1]
                } 
           )
   
    actual_df = audit_column_constraint("initial_df", table_name, column, sql_constraint_predicate)
    

    polars_testing.assert_frame_equal(actual_df, expected_df, check_dtype=False)


if __name__ == "__main__":
    pytest.main()
    
    
