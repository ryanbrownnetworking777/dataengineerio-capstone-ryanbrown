import pytest
from ..src.common.common_data_loading import check_if_allowed, function_not_allowed, read_from_local_duck_db 


def test_check_if_allowed():
    allowed_function = "read_from_local_duck_db"
    not_allowed_function = "unauthorized_function"
    def unauthorized_function():
        return "phoink"
    assert check_if_allowed(allowed_function) == eval(allowed_function), "Allowed function did not return correctly"

    
    assert check_if_allowed(not_allowed_function) == function_not_allowed, "Not allowed function did not return function_not_allowed"


if __name__ == "__main__":
    pytest.main()
