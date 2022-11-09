# Задание 2. Вывести книги, относящиеся к заданному жанру, изданные позже
# заданного года. Указать их издательство и год издания. Информацию отсортировать сначала
# по убыванию года издания, потом по названиям книг в алфавитном порядке.

import sqlite3

# устанавливаем соединение с бд
con = sqlite3.connect("library.sqlite")
# создаем курсор
cursor = con.cursor()

# выбираем и выводим записи из таблиц author, reader
cursor.execute('''
 SELECT
 title,
 publisher_name,
 year_publication
 FROM book
 JOIN genre USING (genre_id)
 JOIN publisher USING (publisher_id)
 WHERE genre_name = :p_genre AND year_publication > :p_year
''', {"p_genre": "Детектив", "p_year": 2016})
print(cursor.fetchall())

# Средствами SQLite Python реализовать выборку следующих данных.
# 1. Для каждого жанра посчитать, сколько различных книг этого жанра представлено в
# библиотеке, каково общее количество доступных экземпляров книг (имеющихся в наличии)
# и какой самый ранний год издания книг, относящихся к этому жанру. Информацию
# отсортировать по названию жанра в алфавитном порядке.
cursor.execute('''
    SELECT genre_name, COUNT(*), SUM(available_numbers), MIN(year_publication)
    FROM book
    INNER JOIN genre g on book.genre_id = g.genre_id
    GROUP BY genre_name
    ORDER BY genre_name
''')
print(cursor.fetchall())

# 2. Вывести информацию о всех книгах, который сдал заданный читатель. Для каждой
# книги указать дату выдачи, дату сдачи и сколько дней книга была на руках. Информацию
# отсортировать по убыванию количества дней (В SQLite нет функции DATEDIFF,
# самостоятельно найти способ реализации этой функции).
cursor.execute('''
    SELECT 
        title, 
        borrow_date, 
        return_date, 
        JULIANDAY(return_date) - JULIANDAY(borrow_date) + 1 days_num
    FROM book
    INNER JOIN book_reader br on book.book_id = br.book_id
    INNER JOIN reader r on r.reader_id = br.reader_id
                        AND reader_name = :p_reader_name
    WHERE return_date IS NOT NULL 
    ORDER BY days_num DESC
''', {"p_reader_name": "Петров Ф.С."})
print(cursor.fetchall())

# 3. Вывести самый популярный жанр (жанры). Самым популярным считается жанр,
# книги которого чаще всего брали читатели в библиотеке. Вывести название жанра (жанров) и
# сколько раз читатели брали книги этого жанра. Информацию отсортировать по названию
# жанров в алфавитном порядке.
cursor.execute('''
    SELECT genre_name, COUNT(borrow_date) amount
    FROM genre
    INNER JOIN book b on genre.genre_id = b.genre_id
    INNER JOIN book_reader br on b.book_id = br.book_id
    GROUP BY genre_name
    ORDER BY amount DESC, genre_name
    LIMIT 1
''')
print(cursor.fetchall())

# закрываем соединение с базой
con.close()
