# Объект-шаблон из модуля jinja2
from jinja2 import Template
# Модуль для построения графиков
import matplotlib.pyplot as plt


# Вычислить значение заданной функции при аргументе x
def f(x, n_var):
    if n_var == 0:
        y = x ** 3 - 6 * x ** 2 + x + 5
    elif n_var == 1:
        y = x ** 2 - 5 * x + 1
    elif n_var == 2:
        y = 1 / (x ** 2 + 1)
    return y


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
    plt.savefig("pict_func.jpg")

    # Вернуть имя созданного файла
    return "pict_func.jpg"


# Номер варианта функции
n_var = int(input("Введите номер функции от 0 до 2: "))

# Список с названиями функций
list_name_f = ["f(x)", "y(x)", "z(x)"]

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
f_list = [f(x, n_var) for x in x_list]

# Сохранить график функции в файл
name_pict = create_pict(x_list, f_list)

# Прочитать шаблон из файла functions_template.html
f_template = open('functions_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

# Прочитать шаблон из файла function_block_template.html
f_template = open('function_block_template.html', 'r', encoding='utf-8-sig')
html_block = f_template.read()
f_template.close()

# Создать объект-шаблон
template = Template(html)
template_block = Template(html_block)

# Указать, что в шаблоне будут использованы функции
template.globals["len"] = len
template.globals["round"] = round

# Файл для HTML-страницы
f = open('functions.html', 'w', encoding='utf-8-sig')

# Сгенерировать страницу на основе шаблона
result_html = template.render(x=x_list,
                              y=f_list,
                              pict=name_pict,
                              count_f=len(list_name_f),
                              n_var=n_var,
                              list_f=list_name_f,
                              a=a,
                              b=b,
                              n=n,
                              len=len,
                              round=round,
                              template=template_block)

# Вывести сгенерированную страницу в файл
f.write(result_html)
f.close()
