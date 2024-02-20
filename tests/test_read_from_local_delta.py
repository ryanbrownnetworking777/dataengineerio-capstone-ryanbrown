import shutil
import os
import pytest
import polars.testing as polars_testing
import polars as pl
from ..src.common.common_data_loading import write_to_local_delta, read_from_local_delta

def test_read_from_local_delta():
    delta_lake_path = "test_delta_lake"
    layer = "test_layer"
    table_name = "test_table"
    df = pl.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})

    
    write_to_local_delta(delta_lake_path, layer, table_name, df)

    
    delta_table_path = os.path.join(delta_lake_path, layer, table_name)
    read_df = read_from_local_delta(delta_lake_path, layer, table_name) 

    
    polars_testing.assert_frame_equal(df.lazy(), read_df)

    shutil.rmtree(delta_table_path)

if __name__ == "__main__":
    pytest.main()
