import pytest
from ..src.common.common_data_loading import load_sql_query  


def setup_test_sql_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


def test_load_sql_query():
    query_path = ["test_query.sql"]
    expected_query = "SELECT * FROM test_table;"
    setup_test_sql_file(query_path[0], expected_query)

    
    loaded_query = load_sql_query(query_path)

    assert loaded_query == expected_query, "The function did not load the expected query."


if __name__ == "__main__":
    pytest.main()
