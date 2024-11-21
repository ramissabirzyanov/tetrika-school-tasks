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


URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'


def write_to_scv(*args):
    with open('task2/beasts.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(args)


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text


def get_data_from_first_page(url):
    page = get_html(url)
    soup = BeautifulSoup(page, 'html.parser')
    div_tag = soup.find('div', 'mw-category mw-category-columns').find_all('div', 'mw-category-group')
    data = {tag.find('h3').text: len(tag.find_all('li')) for tag in div_tag}
    next_page = soup.find(string='Следующая страница').parent.get('href')
    next_page_url = 'https://ru.wikipedia.org' + next_page
    return data, next_page_url


def get_animals_count(url=URL):
    alphabet = dict.fromkeys([chr(i) for i in range(ord('А'), ord('Я')+1)], 0)
    data, next_url = get_data_from_first_page(url)
    for letter, count in data.items():
        if letter in alphabet:
            alphabet[letter] += count
            get_data_from_first_page(next_url)
        else:
            return alphabet

