import pandas


# Активность читателей в заданный период (сколько книг взяли и какие)
def get_reader_activity(conn, start_date, finish_date):
    return pandas.read_sql(f'''
SELECT reader_name Читатель, 
       group_concat(DISTINCT title) Книги, 
       count(*) Выдано_экземпляров
FROM book b
         INNER JOIN book_reader USING (book_id)
         INNER JOIN reader USING (reader_id)
WHERE borrow_date BETWEEN '{start_date}' AND '{finish_date}'
GROUP BY reader_id
''', conn)
