# Когда пользователь заходит на страницу урока, мы сохраняем время его захода.
# Когда пользователь выходит с урока (или закрывает вкладку, браузер –
# в общем как-то разрывает соединение с сервером),
# мы фиксируем время выхода с урока.
# Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов.
# В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):
# lesson – начало и конец урока
# pupil – интервалы присутствия ученика
# tutor – интервалы присутствия учителя
# Интервалы устроены следующим образом –
# это всегда список из четного количества элементов.
# Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
# Нужно написать функцию appearance,
# которая получает на вход словарь с интервалами и
# возвращает время общего присутствия ученика и учителя на уроке (в секундах).


def get_online_seconds(lesson_interval: list, person_interval: list) -> list:
    online_sec = []
    lesson_seconds = [sec for sec in range(lesson_interval[0], lesson_interval[1])]
    while person_interval:
        interval_begin = person_interval.pop(0)
        interval_end = person_interval.pop(0)
        person_seconds = [num for num in range(interval_begin, interval_end)]
        for second in person_seconds:
            if second in lesson_seconds:
                online_sec.append(second)
    return online_sec


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_interval = intervals['lesson']
    tutor_interval = intervals['tutor']
    pupil_interval = intervals['pupil']
    tutor_online_sec = get_online_seconds(lesson_interval, tutor_interval)
    pupil_online_sec = get_online_seconds(lesson_interval, pupil_interval)
    return len(set(tutor_online_sec).intersection(pupil_online_sec))


tests = [
    {'intervals': {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
     'answer': 3117},
    {'intervals': {
        'lesson': [1594702800, 1594706400],
        'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
        'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
     'answer': 3577},
    {'intervals': {
        'lesson': [1594692000, 1594695600],
        'pupil': [1594692033, 1594696347],
        'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565},
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
