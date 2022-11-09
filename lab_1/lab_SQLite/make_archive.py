import sqlite3

# устанавливаем соединение с бд
con = sqlite3.connect("library.sqlite")
# создаем объект-курсор
cursor = con.cursor()

# cursor.executescript('''
#     CREATE TABLE IF NOT EXISTS archive(
#     book_id INTEGER PRIMARY KEY,
#     title VARCHAR(50),
#     authors VARCHAR(100),
#     lost INTEGER
#     );
#
#     INSERT INTO archive(book_id, title, authors, lost)
#     SELECT book_id, title , GROUP_CONCAT(author_name,', ') authors, available_numbers as lost
#     FROM book
#     JOIN book_author USING (book_id)
#     JOIN author USING (author_id)
#     WHERE available_numbers = 0
#     GROUP BY book_id;
#
#     INSERT INTO archive(book_id, title, authors, lost)
#     SELECT book_id, title, authors , COUNT(*) lost
#     FROM
#     (SELECT book_id, title , GROUP_CONCAT(author_name,', ') authors, available_numbers as lost
#     FROM book
#     JOIN book_author USING (book_id)
#     JOIN author USING (author_id)
#     WHERE available_numbers != 0
#     GROUP BY book_id)
#     JOIN book_reader USING (book_id)
#     WHERE return_date is null
#     GROUP BY book_id;
# ''')
con.commit()

# вот есть у меня таблица archive, а в ней столбец lost, также есть в таблице book столбец available_numbers,
# так вот мне надо столбец available_numbers обновить так, чтобы бы значение там стало available_numbers - lost
cursor.execute('''
    UPDATE book
    SET available_numbers = available_numbers - lost
    FROM archive
    WHERE book.book_id = archive.book_id
''')
con.commit()

con.close()
