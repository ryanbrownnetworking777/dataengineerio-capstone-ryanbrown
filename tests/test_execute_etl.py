import pytest
from unittest.mock import MagicMock
from ..src.common.common_data_loading import * 



def mock_function(**kwargs):
    return "mock_result"


def test_execute_etl():
    to_execute_list = [
        {
            'step_description': 'Test Step 1',
            'function_to_execute': 'mock_function',
            'function_to_execute_arguments': {'arg1': 'value1'}
        },
        {
            'step_description': 'Test Step 2',
            'function_to_execute': 'disallowed_function',
            'function_to_execute_arguments': {'arg2': 'value2'}
        }
    ]
    

    global allowed_functions
    print(allowed_functions)
    allowed_functions += ["mock_function"]
    print(allowed_functions)
    expected_result = ['mock_result', 'The function passed is not in the allowed function list so this function, `function_not_allowed`, has been substituted instead']  
    actual_result =  execute_etl(to_execute_list)
    assert actual_result == expected_result 

if __name__ == "__main__":
    pytest.main()
