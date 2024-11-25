import pytest
from task1.solution import strict


@strict
def sum_two(a: float, b: float) -> int:
    return a + b


@pytest.mark.parametrize("arg1, arg2, expected", [
    (1, 2, 3),
    (1, 2.4, pytest.raises(TypeError)),
    ])
def test_strict_decorator(arg1, arg2, expected):
    with pytest.raises(TypeError):
        assert sum_two(arg1, arg2) == expected
