import sqlite3
import pandas as pd

# устанавливаем соединение с бд
con = sqlite3.connect("lib.sqlite")
# создаем объект-курсор
cursor = con.cursor()

# Отобрать информацию о книгах, количество которых больше 3. Столбцы назвать
# Книга, Жанр, Издательство и Количество.
# Вывести отобранную информацию:
df = pd.read_sql('''
    SELECT
        title Книга,
        genre_name Жанр,
        publisher_name Издательство,
        available_numbers Количество
    FROM book
    JOIN genre USING (genre_id)
    JOIN publisher USING (publisher_id)
    WHERE available_numbers > :p_num
''', con, params={"p_num": 3})

# - в виде таблицы;
print(df, '\n')

# - только столбец Название;
print(df["Книга"], '\n')

# - 3-ю строку результата запроса;
print(df.loc[3], '\n')

# - количество строк и столбцов в результате запроса;
print("Количество строк:", df.shape[0], '\n')
print("Количество столбцов:", df.shape[1], '\n')

# - названия столбцов.
print(df.dtypes.index)

con.close()
