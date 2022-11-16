import pandas as pd


def get_publisher(conn):
    return pd.read_sql('''
        SELECT publisher_name, 
        count(book_id) 
        FROM publisher p
        INNER JOIN book b on p.publisher_id = b.publisher_id
        GROUP BY publisher_name''', conn)


def get_genre(conn):
    return pd.read_sql('''
        SELECT genre_name, 
        count(book_id) 
        FROM genre g
        INNER JOIN book b on g.genre_id = b.genre_id
        GROUP BY genre_name''', conn)


def get_author(conn):
    return pd.read_sql('''
        SELECT author_name, 
        count(b.book_id) 
        FROM author a
        INNER JOIN book_author ba on a.author_id = ba.author_id
        INNER JOIN book b on b.book_id = ba.book_id
        GROUP BY author_name''', conn)


def get_book(conn, genres, authors, publishers):
    return pd.read_sql(f'''
SELECT b.book_id,
       title                              Название,
       group_concat(DISTINCT author_name) Авторы,
       genre_name                         Жанр,
       publisher_name                     Издательство,
       year_publication                   Год_издания,
       available_numbers                  Количество
FROM book b
         INNER JOIN book_author ba on b.book_id = ba.book_id
         INNER JOIN author a on a.author_id = ba.author_id
         INNER JOIN genre g on g.genre_id = b.genre_id
    AND (genre_name IN ({str(genres).strip('[]')}) OR {not genres})
         INNER JOIN publisher p on p.publisher_id = b.publisher_id
    AND (publisher_name IN ({str(publishers).strip('[]')}) OR {not publishers})
GROUP BY b.book_id
HAVING (author_name IN ({str(authors).strip('[]')})
    OR {not authors})
    ''', conn)
