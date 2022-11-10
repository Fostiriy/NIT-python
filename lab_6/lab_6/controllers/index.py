import lab_6.lab_6.constants as constants
from lab_6.lab_6.app import app
from flask import render_template


@app.route('/', methods=['GET'])
def index():
    # выводим форму
    html = render_template('index.html',
                           program_list=constants.programs,
                           subject_list=constants.subjects,
                           event_list=constants.events,
                           len=len
                           )
    return html
