import pytest
from ..src.common.common_data_loading import function_not_allowed  


def test_function_not_allowed():
    expected_result =  "The function passed is not in the allowed function list so this function, `function_not_allowed`, has been substituted instead"
    actual_result = function_not_allowed()
    assert actual_result == expected_result, "The actual and expected results are not equal."

if __name__ == "__main__":
    pytest.main()
