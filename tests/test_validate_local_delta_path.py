import shutil
import os
import pytest
import polars.testing as polars_testing
import polars as pl
from ..src.common.common_data_loading import validate_local_delta_path  


def validate_local_delta_path_exists():
    delta_lake_path = "test_delta_lake"
    layer = "test_layer"
    table_name = "test_table"

    delta_lake_path = os.path.join(os.getcwd(),delta_lake_path,layer)
    delta_table_path = os.path.join(delta_lake_path, table_name)

    os.mkdir(delta_table_path)  

    validated_path = validate_local_delta_path(delta_lake_path, layer, table_name) 

    shutil.rmtree(delta_table_path)

    assert delta_lake_path == validated_path, "The paths aren't equal"     

def validate_local_delta_path_does_not_exist():
    delta_lake_path = "test_delta_lake"
    layer = "test_layer"
    table_name = "test_table"

    delta_lake_path = os.path.join(os.getcwd(),delta_lake_path,layer)
    delta_table_path = os.path.join(delta_lake_path, table_name)


    validated_path = validate_local_delta_path(delta_lake_path, layer,table_name) 

    shutil.rmtree(delta_table_path)

    assert delta_lake_path == validated_path, "The paths aren't equal"     



if __name__ == "__main__":
    pytest.main()
