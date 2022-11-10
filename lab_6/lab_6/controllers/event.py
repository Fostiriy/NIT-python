import constants
from app import app
from flask import render_template, request


@app.route('/event/<event_name>')
def event(event_name):
    html = render_template(
        'event.html',
        event_name=event_name,
        discription=constants.event_dict[event_name]
    )
    return html
