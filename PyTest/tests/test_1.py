import pytest


def double(x: int) -> int:
    if not isinstance(x, int):
        raise ValueError("Value cannot be a string!")

    return x * 2


def test_function_double():
    actual_result = double(5)

    assert actual_result == 10


def test_function_double_parameter_not_int():
    with pytest.raises(ValueError):
        double(x="text")

    with pytest.raises(ValueError):
        double(x=1.234)
