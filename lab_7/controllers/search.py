from app import app
from flask import render_template, request
from utils import get_db_connection
from models.search_model import get_genre, get_author, get_publisher, get_book


@app.route('/search', methods=['GET', 'POST'])
def search():
    # устанавливаем соединение с базой данных
    conn = get_db_connection()

    # выполняем запросы к БД
    df_genre = get_genre(conn)
    df_author = get_author(conn)
    df_publisher = get_publisher(conn)

    if request.form.get('clear'):
        genres = []
        publishers = []
        authors = []
    else:
        genres = request.form.getlist('genres')
        publishers = request.form.getlist('publishers')
        authors = request.form.getlist('authors')

    df_book = get_book(conn, genres, authors, publishers)

    # выводим форму
    html = render_template(
        'search.html',
        sections=['genres', 'authors', 'publishers'],
        all_data=[df_genre, df_author, df_publisher],
        all_choices=[genres, authors, publishers],
        books=df_book,
        genre_list=genres,
        authors=authors,
        publishers=publishers,
        len=len,
        zip=zip,
    )
    return html
