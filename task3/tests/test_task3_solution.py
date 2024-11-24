from task3.solution import appearance


fixtures = [
    {'intervals': {
        'lesson': [100, 400],
        'pupil': [90, 110, 200, 290, 300, 420],
        'tutor': [110, 200, 300, 380]},
     'expected': 80},
    {'intervals': {
        'lesson': [100, 400],
        'pupil': [],
        'tutor': [110, 200, 300, 380]},
     'expected': 0},
]


excepted = 80

for fixture in fixtures:
    result = appearance(fixture['intervals'])
    assert result == fixture['expected'], f'Результат = {result}, а ожидается  {fixture['expected']}'
