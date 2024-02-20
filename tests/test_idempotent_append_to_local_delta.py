import shutil
import os
import pytest
import polars.testing as polars_testing
import polars as pl
from ..src.common.common_data_loading import write_to_local_delta, idempotent_append_to_local_delta

def test_idempotent_append_to_local_delta():
    delta_lake_path = "test_delta_lake"
    layer = "test_layer"
    table_name = "test_table"
    initial_df = pl.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    to_append_df = pl.DataFrame({"id": [3, 4], "name": ["Fredrick", "Daisuke"]})
    total_df = pl.DataFrame({"id": [1,2,3,4], "name": ["Alice", "Bob","Fredrick", "Daisuke"]})
    
    write_to_local_delta(delta_lake_path, layer, table_name, initial_df)


    delta_table_path = os.path.join(delta_lake_path, layer, table_name)
    
    idempotent_append_to_local_delta(delta_lake_path, layer, table_name, to_append_df)

    read_df = pl.read_delta(delta_table_path)

    
    shutil.rmtree(delta_table_path)

    
    polars_testing.assert_frame_equal(total_df.sort("id"), read_df.sort("id"))


if __name__ == "__main__":
    pytest.main()

