# Объект-шаблон из модуля jinja2
from jinja2 import Template
# Модуль для построения графиков
import matplotlib.pyplot as plt


# Вычислить значение заданной функции при аргументе x
def f(x):
    return x ** 3 - 6 * x ** 2 + x + 5


# Построение графика по спискам координат x и y
def create_pict(x_list, y_list):
    # Построить линию графика, установить для нее цвет и толщину:
    line = plt.plot(x_list, y_list)
    plt.setp(line, color="blue", linewidth=2)

    # Вывести 2 оси, установить их в позицию zero:
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    # Сохранить результат построения в файл:
    plt.savefig("pict.jpg")

    # Вернуть имя созданного файла
    return "pict.jpg"


# Интервал [a, b]
a = -2
b = 6

# Количество точек построения
n = 30

# Вычислить шаг
h = (b - a) / (n - 1)

# Список со значениями аргумента
x_list = [a + h * i for i in range(n)]

# Список со значениями функции на интервале
f_list = [f(x) for x in x_list]

# Сохранить график функции в файл
name_pict = create_pict(x_list, f_list)

# Прочитать шаблон из файла function_template.html
f_template = open('function_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

# Создать объект-шаблон
template = Template(html)

# Указать, что в шаблоне будут использованы функции
template.globals["len"] = len
template.globals["round"] = round

# Файл для HTML-страницы
f = open('function.html', 'w', encoding='utf-8-sig')

# Сгенерировать страницу на основе шаблона
result_html = template.render(x=x_list, y=f_list, pict=name_pict)

# Вывести сгенерированную страницу в файл
f.write(result_html)
f.close()
