import os
import duckdb
import polars.testing as polars_testing
import polars as pl
import pytest
from ..src.common.common_data_loading import read_from_local_duck_db  


def setup_test_db(db_path):
    conn = duckdb.connect(db_path)
    conn.execute("CREATE OR REPLACE TABLE test_table (id LONG, name VARCHAR)")
    conn.execute("INSERT INTO test_table VALUES (1, 'Alice'), (2, 'Bob')")
    conn.close()


def test_read_from_local_duck_db():
    db_path = "test_db.duckdb"
    query = "SELECT * FROM test_table"
    expected_result = pl.DataFrame([{"id":1, "name":'Alice'}, {"id":2, "name":'Bob'}])

    
    setup_test_db(db_path)


    result = read_from_local_duck_db(db_path, query)

    os.remove(db_path)
    
    polars_testing.assert_frame_equal(result, expected_result)


if __name__ == "__main__":
    pytest.main()
