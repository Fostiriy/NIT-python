import lab_6.lab_6.constants as constants
from lab_6.lab_6.app import app
from flask import render_template, request


@app.route('/event/<event_name>')
def event(event_name):
    html = render_template(
        'event.html',
        event_name=event_name,
        discription=constants.event_dict[event_name]
    )
    return html
