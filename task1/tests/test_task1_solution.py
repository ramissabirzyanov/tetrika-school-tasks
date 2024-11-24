import pytest
from task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


assert sum_two(1, 2) == 3


def test_type_error():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)
