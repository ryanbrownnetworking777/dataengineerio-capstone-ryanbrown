from ..src.common.common_data_loading import mock_function


def test_mock_function():
    expected_result = "mock_result"

    actual_result = mock_function()

    assert actual_result == expected_result, "Actual and expected results are not equal"


if __name__ == "__main__":
    pytest.main()
