import pytest
import duckdb
import polars.testing as polars_testing
import polars as pl
from datetime import datetime
from ..src.common.common_data_loading import check_missing_values

def test_check_missing_values():
    as_of_datetime = datetime.now()
    table_name = "test_table"
    columns = ["id", "name"]
    initial_df = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", None]}).lazy()

    expected_df = pl.DataFrame(
            {
                 "Table Name": [table_name for column in columns] 
                ,"Table Column" : columns
                ,"Null Count": [0,1]
                ,"As Of Datetime" : [as_of_datetime for column in columns]
                } 
           )
   
    actual_df = check_missing_values(initial_df, table_name)
    
    actual_df_for_testing = actual_df.drop("As Of Datetime")
    expected_df_for_testing = expected_df.drop("As Of Datetime")

    polars_testing.assert_frame_equal(actual_df_for_testing, expected_df_for_testing, check_dtype=False)


if __name__ == "__main__":
    pytest.main()
    
    
