from app import app
from flask import render_template, request

from models.statistics_model import get_reader_activity
from utils import get_db_connection


@app.route('/statistics', methods=['get', 'post'])
def statistics():
    conn = get_db_connection()

    table_name = ""
    df_query = ""
    id_name = ""

    # нажата кнопка Найти
    if request.values.get('query'):
        query = request.values.get('query')
        start_date = request.values.get('start_date')
        finish_date = request.values.get('finish_date')

        if query == "reader_activity":
            table_name = "Активность читателей"
            df_query = get_reader_activity(conn, start_date, finish_date)

    # выводим форму
    html = render_template(
        'statistics.html',
        table_name=table_name,
        df_query=df_query,
        id=id_name,
        len=len
    )
    return html
