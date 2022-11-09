import sqlite3

# устанавливаем соединение с бд
con = sqlite3.connect("lib.sqlite")
# создаем объект-курсор
cursor = con.cursor()

# 1. Вывести книги (указать их жанр), количество которых принадлежит интервалу от a
# до b, включая границы (границы интервала передать в качестве параметра).
cursor.execute('''
    SELECT title, genre_name, available_numbers
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    WHERE available_numbers BETWEEN :p_beg AND :p_end;
''', {"p_beg": 7, "p_end": 9})
print(cursor.fetchall())

# 2. Вывести книги (указать их издательство), название которой состоит из одного
# слова, и книга издана после заданного года (год передать в качестве параметра).
cursor.execute('''
    SELECT title, publisher_name, year_publication
    FROM book
    JOIN publisher USING (publisher_id)
    WHERE title NOT LIKE "% %"
          AND year_publication > :p_year
''', {"p_year": 2015})
print(cursor.fetchall())

# 3. Вычислить, сколько экземпляров книг каждого жанра представлены в библиотеке.
# Учитывать только книги, изданные после заданного года (год передать в качестве
# параметра).
cursor.execute('''
    SELECT genre_name, SUM(available_numbers)
    FROM book
    JOIN genre USING (genre_id)
    WHERE year_publication > :p_year
    GROUP BY genre_name
''', {"p_year": 2000})
print(cursor.fetchall())

con.close()
