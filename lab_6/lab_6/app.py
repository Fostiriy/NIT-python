from flask import Flask

app = Flask(__name__)

app.debug = True

# здесь должны импортироваться все программы-контроллеры,
# размещенные в папке controllers
import controllers.index
import controllers.hello
import controllers.subject
import controllers.event

app.run(host='localhost', port=5000)
