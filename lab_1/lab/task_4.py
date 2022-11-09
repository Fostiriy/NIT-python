import sqlite3
import pandas as pd

# устанавливаем соединение с бд
con = sqlite3.connect("lib.sqlite")
# создаем объект-курсор
cursor = con.cursor()

# 1. Создать кортеж, в который включить название двух издательств. Реализовать
# запрос, который выводит книги издательств, входящих в кортеж, изданных с 2016 по 2019
# года, включая границы.
publisher_list = ("АСТ", "ДРОФА")
df = pd.read_sql(f'''
    SELECT
        title Книга,
        publisher_name Издательство,
        year_publication Год_публикации
    FROM book
    JOIN genre USING (genre_id)
    JOIN publisher ON book.publisher_id = publisher.publisher_id
                      AND publisher_name IN {publisher_list}
    WHERE year_publication BETWEEN :p_beg AND :p_end
''', con, params={"p_beg": 2016, "p_end": 2019})
print(df)

con.close()
