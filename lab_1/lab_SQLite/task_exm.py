import sqlite3
import pandas as pd

# устанавливаем соединение с бд
con = sqlite3.connect("library.sqlite")
# создаем объект-курсор
cursor = con.cursor()

cursor.execute(f'''
    DELETE FROM book_reader
    WHERE book_reader_id = 46
''')

# Найти человека, который не брал ни одной книги
# Занести его в таблицу book_reader со случайно выбранной книгой и текущей датой выдачи книги

df = pd.read_sql('''
    SELECT 
        r.reader_id,
        r.reader_name
    FROM reader r
    LEFT JOIN book_reader br on r.reader_id = br.reader_id
    WHERE br.reader_id IS NULL
''', con)
print(df, '\n')

cursor.execute(f'''
    INSERT INTO book_reader(book_id, reader_id, borrow_date)
    SELECT 
        (SELECT book_id FROM book ORDER BY RANDOM() LIMIT 1),
        r.reader_id,
        date('now')
    FROM reader r
    LEFT JOIN book_reader br on r.reader_id = br.reader_id
    WHERE br.reader_id IS NULL
''')
con.commit()

df = pd.read_sql('''
    SELECT * FROM book_reader
''', con)
print(df, '\n')

# Для тех читателей, которые не сдали книги рекомендовать в какой день они должны сдать эти книги
# по следующему алгоритму: нужно сдать в ближайший вторник через 14 дней, и создать таблицу для этих людей,
# куда включить фамилию и дату
cursor.execute(f'''
    CREATE TABLE expected_return AS
    SELECT
        reader_name,
        iif(strftime('%w', borrow_date) IN ('3', '4', '5'), date(borrow_date, 'weekday 2', '7 days'), date(borrow_date, '14 days', 'weekday 2'))
    FROM book_reader br
    INNER JOIN reader r on r.reader_id = br.reader_id
    WHERE return_date IS NULL
''')
con.commit()

con.close()
