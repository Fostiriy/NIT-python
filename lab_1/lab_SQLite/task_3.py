# Задание 3. Вывести в виде таблицы результат следующей выборки (использовать
# модуль pandas и DataFrame). Найти книги, относящиеся к заданному жанру, изданные
# позже заданного года. Указать их издательство и год издания. Столбцы назвать Название,
# Издательство, Год соответственно. Информацию отсортировать сначала по убыванию
# года издания, потом по названиям книг в алфавитном порядке.

import sqlite3
import pandas as pd

# устанавливаем соединение с бд
con = sqlite3.connect("library.sqlite")

# выбираем и выводим записи из таблиц author, reader
df = pd.read_sql('''
 SELECT
 title AS Название,
 publisher_name AS Издательство,
 year_publication AS Год
 FROM book
 JOIN genre USING (genre_id)
 JOIN publisher USING (publisher_id)
 WHERE genre_name = :p_genre AND year_publication > :p_year
''', con, params={"p_genre": "Роман", "p_year": 2016})
print(df, '\n')

# Средствами SQLite Python реализовать выборку следующих данных.
# 1. Вывести книги, которые были взяты в библиотеке в октябре месяце. Указать
# фамилии читателей, которые их взяли, а также дату, когда их взяли. Столбцы назвать
# Название, Читатель, Дата соответственно. Информацию отсортировать сначала по
# возрастанию даты, потом в алфавитном порядке по фамилиям читателей, и, наконец, по
# названиям книг тоже в алфавитном порядке.
df = pd.read_sql('''
    SELECT 
        title Название,
        substring(reader_name, 1, length(reader_name) - 5) Читатель,
        borrow_date Дата
    FROM book
    INNER JOIN book_reader br on book.book_id = br.book_id
                             AND strftime('%m', borrow_date) = :p_month
    INNER JOIN reader r on r.reader_id = br.reader_id
    ORDER BY Дата, Читатель, Название
''', con, params={"p_month": "10"})
print(df, '\n')

# 2. Для каждой книги, изданной в заданном издательстве, вывести информацию о ее
# принадлежности к группе:
# * если книга издана раньше 2014 года, вывести "III";
# * если книга издана в период с 2014 года по 2017 год, вывести "II";
# * если книга издана позже 2017 года, вывести "I".
df = pd.read_sql('''
    SELECT 
        title Название,
        iif(year_publication < 2014, 'III', iif(year_publication BETWEEN 2014 AND 2017, 'II', 'I')) Группа
    FROM book
    INNER JOIN publisher p on book.publisher_id = p.publisher_id
    WHERE publisher_name = :p_publisher_name
''', con, params={"p_publisher_name": "ДРОФА"})
print(df, '\n')

# 3. Для каждой книги также указать ее жанр и год издания. Столбцы назвать
# Название, Жанр, Год, Группа. Информацию отсортировать сначала по группе в
# порядке убывания, потом возрастанию года издания и, наконец, по названию в алфавитном
# порядке.
df = pd.read_sql('''
    SELECT 
        title Название,
        genre_name Жанр,
        year_publication Год,
        iif(year_publication < 2014, 'III', iif(year_publication BETWEEN 2014 AND 2017, 'II', 'I')) Группа
    FROM book
    INNER JOIN publisher p on book.publisher_id = p.publisher_id
    INNER JOIN genre g on book.genre_id = g.genre_id
    WHERE publisher_name = :p_publisher_name
    ORDER BY Группа DESC, Год, Название
''', con, params={"p_publisher_name": "ДРОФА"})
print(df, '\n')

# 4. Для каждой книги вывести количество экземпляров, которые есть в наличии
# (available_numbers) в библиотеке, а также сколько раз экземпляры книги брали
# читатели. Если книгу читатели не брали - вывести 0. Столбцы назвать Название,
# Количество, Количество_выдачи. Информацию отсортировать сначала по убыванию
# количества выданных экземпляров, а потом по названию книги в алфавитном порядке и,
# наконец, по возрастанию доступного количества.
df = pd.read_sql('''
    SELECT 
        title Название,
        available_numbers Количество,
        iif(COUNT(borrow_date) IS NOT NULL, COUNT(borrow_date), 0) Количество_выдачи
    FROM book
    LEFT JOIN book_reader br on book.book_id = br.book_id
    GROUP BY Название, Количество
    ORDER BY Количество_выдачи DESC, Название, Количество
''', con)
print(df, '\n')

# закрываем соединение с базой
con.close()
