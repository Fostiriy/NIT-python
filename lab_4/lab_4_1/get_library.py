# импортируем необходимые модули
from jinja2 import Template
import sqlite3
from library_model import get_publisher, get_genre, get_reader, get_author, get_book, get_book_reader, get_book_author

# устанавливаем соединение с базой данных (базу данных взять из ЛР 1)
conn = sqlite3.connect("../library.sqlite")

# заносим названия таблиц для вывода
table_names = ['publisher', 'genre', 'reader', 'author', 'book_author', 'book', 'book_reader']

# выбираем записи из таблиц
relations = [get_publisher(conn), get_genre(conn), get_reader(conn), get_author(conn), get_book_author(conn),
             get_book(conn), get_book_reader(conn)]

# закрываем соединение с базой
conn.close()

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('library_templ.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона
result_html = template.render(
    table_names=table_names,
    relations=relations,
    len=len,
    zip=zip
)

# создаем файл для HTML-страницы
f = open('library.html', 'w', encoding='utf-8-sig')

# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
