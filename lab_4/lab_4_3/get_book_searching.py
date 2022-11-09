from jinja2 import Template
import sqlite3
import book_searching_model as m

# устанавливаем соединение с базой данных
conn = sqlite3.connect("../library.sqlite")

# выполняем запросы к БД
df_genre = m.get_genre(conn)
df_author = m.get_author(conn)
df_publisher = m.get_publisher(conn)

genre_list = ('Детектив', 'Приключения', 'Роман')
authors = ('Агата Кристи', 'Жюль Верн', 'Ильф И.А.', 'Петров Е.П.')
publishers = ()

# genre_list = ()
# authors = ('Ильф И.А.', '')
# publishers = ()

df_book = m.get_book(conn)

# закрываем соединение с базой
conn.close()

# открываем файл reader_book_templ.html и читаем шаблон
f_template = open('book_searching_templ.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона
result_html = template.render(
    section_names=['Жанр', 'Автор', 'Издательство'],
    all_data=[df_genre, df_author, df_publisher],
    all_choices=[genre_list, authors, publishers],
    books=df_book,
    genre_list=genre_list,
    authors=authors,
    publishers=publishers,
    len=len,
    zip=zip,
    list=list,
    set=set,
)

# создаем файл для HTML-страницы
f = open('book_searching.html', 'w', encoding='utf-8-sig')

# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
