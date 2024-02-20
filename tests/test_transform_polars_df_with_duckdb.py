import os
import pytest
import polars.testing as polars_testing
import polars as pl
import duckdb
from ..src.common.common_data_loading import transform_polars_df_with_duckdb, load_sql_query  


def setup_test_sql_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


def test_transform_polars_df_with_duckdb():
    query_path = "test_query.sql"
    sql_query = "SELECT id, name FROM test_table WHERE id > 1;"
    setup_test_sql_file(query_path, sql_query)

    
    test_table = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
    expected_transformed_df = pl.DataFrame({"id": [2, 3], "name": ["Bob", "Charlie"]})

    
    transformed_df = transform_polars_df_with_duckdb([query_path])

    
    os.remove(query_path)

    
    polars_testing.assert_frame_equal(transformed_df, expected_transformed_df)


if __name__ == "__main__":
    pytest.main()
