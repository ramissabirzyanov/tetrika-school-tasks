import pytest
from task2.solution import get_animal_count


TEST_URL_1 = 'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=Ящ'
TEST_URL_2 = 'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&filefrom=Ящ&subcatfrom=Ящ&pageuntil=Яблонная+плодожорка#mw-pages'
TEST_URL_3 = 'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Acanthurus+mata&subcatfrom=Ящ&filefrom=Ящ#mw-pages'


@pytest.mark.parametrize("url, expected", [
    (TEST_URL_1, {'Я': 17}),
    (TEST_URL_2, {'Э': 48, 'Ю': 147, 'Я': 222}),
    (TEST_URL_3, {}),
    ])
def test_get_animal_count(url, expected):
    result = get_animal_count(url)
    assert dict(result) == expected
