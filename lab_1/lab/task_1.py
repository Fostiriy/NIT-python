import sqlite3

# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("lib.sqlite")

# создаем таблицы book, genre, publisher, если их еще не было, заносим в них записи
con.executescript('''
    CREATE TABLE IF NOT EXISTS genre(
        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre_name VARCHAR(30)
    );

    INSERT INTO genre (genre_name)
    VALUES
        ('Роман'),
        ('Приключения'),
        ('Детектив'),
        ('Поэзия'),
        ('Фантастика'),
        ('Фэнтези');

    CREATE TABLE IF NOT EXISTS publisher(
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        publisher_name VARCHAR(30)
    );

    INSERT INTO publisher (publisher_name)
    VALUES
        ('ЭКСМО'),
        ('ДРОФА'),
        ('АСТ');

    CREATE TABLE IF NOT EXISTS book(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(30),
        genre_id INT,
        publisher_id INT,
        year_publication INT,
        available_numbers INT,
        FOREIGN KEY (genre_id) REFERENCES genre (genre_id),
        FOREIGN KEY (publisher_id) REFERENCES publisher (publisher_id)
    );

    INSERT INTO book(title, genre_id, publisher_id, year_publication, available_numbers)
    VALUES
        ('Мастер и Маргарита', 1, 2, 2014, 5),
        ('Таинственный остров', 2, 2, 2015, 10),
        ('Бородино', 4, 3, 2015, 12),
        ('Дубровский', 1, 2, 2020, 7),
        ('Вокруг света за 80 дней', 2, 2, 2019, 5),
        ('Убийства по алфавиту', 1, 1, 2017, 9),
        ('Затерянный мир', 2, 1, 2020, 3),
        ('Герой нашего времени', 1, 3, 2017, 2),
        ('Смерть поэта', 4, 1, 2020, 2),
        ('Поэмы', 4, 3, 2019, 5);
 ''')

# сохраняем информацию в базе данных
con.commit()

con.close()
