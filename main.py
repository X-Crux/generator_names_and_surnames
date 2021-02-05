import requests
from bs4 import BeautifulSoup
import random

# парсинг мужских имен
with open('name_list_man.csv', mode='a', encoding='utf8') as file:
    url = 'https://kakzovut.ru/man.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    quotes_tit = soup.findAll("div", {"class": "nameslist"})

    for i in range(len(quotes_tit)):
        file.write(quotes_tit[i].a.text + '\n')

# парсинг женских имен
with open('name_list_woman.csv', mode='a', encoding='utf8') as file:
    url = 'https://kakzovut.ru/woman.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    quotes_tit = soup.findAll("div", {"class": "nameslist"})

    for i in range(len(quotes_tit)):
        file.write(quotes_tit[i].a.text + '\n')

# объедиение мужских и женских имен в общий список
names = ['name_list_man.csv', 'name_list_woman.csv']
with open('names_unite.csv', mode='a', encoding='utf8') as file:
    for i in names:
        with open(i, mode='r', encoding='utf8') as file_csv:
            for j in file_csv:
                file.write(j)

# парсинг фамилий
with open('surname_list.csv', mode='a', encoding='utf8') as file:
    url = 'http://imja.name/familii/pyatsot-chastykh-familij.shtml'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    quotes_tit = soup.findAll("td", {"class": "topin1"})

    for i in range(len(quotes_tit)):
        file.write(quotes_tit[i].text + '\n')

# генерация имя + фамилия
file_names = open('names_unite.csv', mode='r', encoding='utf8')
file_surnames = open('surname_list.csv', mode='r', encoding='utf8')
list_names = list(file_names)
list_surnames = list(file_surnames)
names_surnames = []
with open('names_surnames_list.csv', mode='a', encoding='utf8') as file:
    for i in range(0, 2000):
        file.write(random.choice(list_names)[:-1] + ' ' + random.choice(list_surnames))
file_names.close()
file_surnames.close()
