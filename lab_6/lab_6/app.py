from flask import Flask

app = Flask(__name__)

# здесь должны импортироваться все программы-контроллеры,
# размещенные в папке controllers
import lab_6.lab_6.controllers.index
import lab_6.lab_6.controllers.hello

app.run(host='localhost', port=5000)
