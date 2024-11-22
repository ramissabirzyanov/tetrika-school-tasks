# Необходимо реализовать скрипт,
# который будет получать с русскоязычной википедии список всех животных
# (https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту)
# и записывать в файл в формате beasts.csv количество животных на каждую букву алфавита.
# Содержимое результирующего файла:

# А,642
# Б,412
# В,....

# Примечание:
# анализ текста производить не нужно,
# считается любая запись из категории
# (в ней может быть не только название, но и, например, род)


import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict


URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
SEACH_UNTIL_LETTER = 'A'


def write_to_scv(*args):
    with open('task2/beasts.csv', 'w', newline='') as file:
        for item in args:
            csv.writer(file).writerows(item)


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text


def get_data_from_page(url):
    page = get_html(url)
    soup = BeautifulSoup(page, 'html.parser')
    div_tag = soup.find('div', 'mw-category mw-category-columns').find_all('div', 'mw-category-group')
    data = {tag.find('h3').text: len(tag.find_all('li')) for tag in div_tag
            if tag.find('h3').text != SEACH_UNTIL_LETTER}
    if data:
        next_page = soup.find(string='Следующая страница').parent.get('href')
        next_page_url = 'https://ru.wikipedia.org' + next_page
    else:
        next_page_url = None
    return data, next_page_url


def get_animal_count(url=URL):
    animal_count = defaultdict(int)

    while url:
        data, next_page_url = get_data_from_page(url)
        url = next_page_url
        for letter, count in data.items():
            animal_count[letter] += count

    return animal_count.items()


if __name__ == '__main__':
    animal_count = get_animal_count()
    write_to_scv(animal_count)
