import duckdb
import polars as pl
import os
import yaml
from ..common.common_data_loading import *

"""
This script reads configs from the `{delta_layer}_data_loading_configs.yaml` file and executes the functions called for there along with their arguments.
"""

config_path = [
     "dirs"
    ,"for"
    ,"path"
    ,"to"
    ,"config"
]

def main():
    current_dir = os.getcwd()

    relative_config_file_path = os.path.join(*config_path)

    absolute_config_file_path = os.path.join(current_dir, relative_config_file_path)

    config_file =  open(absolute_config_file_path, "r+").read() 

    config_dict = yaml.safe_load(config_file)

    for etl_job in config_dict["etl_jobs"]:
        execute_etl(etl_job)
    
if __name__ == "__main__":
    main()

    
