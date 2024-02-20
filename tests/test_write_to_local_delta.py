import shutil
import os
import pytest
import polars.testing as polars_testing
import polars as pl
from ..src.common.common_data_loading import write_to_local_delta  


def test_write_to_local_delta():
    delta_lake_path = "test_delta_lake"
    layer = "test_layer"
    table_name = "test_table"
    df = pl.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})

    
    write_to_local_delta(delta_lake_path, layer, table_name, df)

    
    delta_table_path = os.path.join(delta_lake_path, layer, table_name)
    read_df = pl.read_delta(delta_table_path)

    
    shutil.rmtree(delta_table_path)

    
    polars_testing.assert_frame_equal(df, read_df)


if __name__ == "__main__":
    pytest.main()
