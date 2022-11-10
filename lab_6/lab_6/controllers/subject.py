import lab_6.lab_6.constants as constants
from lab_6.lab_6.app import app
from flask import render_template, request


@app.route('/subject/<sub>')
def subject(sub):
    html = render_template(
        'subject.html',
        sub=sub,
        discription=constants.subject_dict[sub]
    )
    return html
