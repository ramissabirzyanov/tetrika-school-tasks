import pytest
from task3.solution import appearance


fixtures_1 = {
    'intervals': {
        'lesson': [100, 400],
        'pupil': [90, 110, 200, 290, 300, 420],
        'tutor': [110, 200, 300, 380]},
    'expected': 80,
}

fixtures_2 = {
    'intervals': {
        'lesson': [100, 400],
        'pupil': [],
        'tutor': [110, 200, 300, 380]},
    'expected': 0,
}


@pytest.mark.parametrize("intervals, expected", [
    (fixtures_1['intervals'], fixtures_1['expected']),
    (fixtures_2['intervals'], fixtures_2['expected']),
    ])
def test_appearance(intervals, expected):
    result = appearance(intervals)
    assert result == expected, f'Результат = {result}, а ожидается  {expected}'
