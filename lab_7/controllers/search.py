from app import app
from flask import render_template


@app.route('/search', methods=['get'])
def search():
    # выводим форму
    html = render_template(
        'search.html',
    )
    return html
