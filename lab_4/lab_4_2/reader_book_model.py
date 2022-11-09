import pandas as pd


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, reader_id):
    return pd.read_sql(f'''
    SELECT title Книга,
    group_concat(author_name) Авторы,
    borrow_date Дата_выдачи, 
    return_date Дата_возврата
    FROM book_reader br
    INNER JOIN book b on b.book_id = br.book_id
    INNER JOIN book_author ba on b.book_id = ba.book_id
    INNER JOIN author a on a.author_id = ba.author_id
    WHERE reader_id = {reader_id}
    GROUP BY title, borrow_date, return_date''', conn)
