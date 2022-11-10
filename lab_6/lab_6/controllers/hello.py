import lab_6.lab_6.constants as constants
from lab_6.lab_6.app import app
from flask import render_template, request


@app.route('/hello', methods=['GET'])
def hello():
    # для каждого передаваемого параметра формы нужно задать
    # значение по умолчание, на случай если пользователь ничего не введет
    name = ""
    gender = ""
    program_id = 0
    # список из номеров выбранных пользователем дисциплин
    subject_id = []
    # список из выбранных пользователем дисциплин
    subjects_select = []
    # список из выбранных пользователем мероприятий
    events_select = []
    name = request.values.get('username')
    gender = request.values.get('gender')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    event_id = request.values.getlist('event[]')
    # формируем список из выбранных пользователем дисциплин
    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    events_select = [constants.events[int(i)] for i in event_id]
    html = render_template(
        'hello.html',
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        len=len,
        subjects_select=subjects_select,
        events_select=events_select,
    )
    return html
