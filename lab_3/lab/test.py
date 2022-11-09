from jinja2 import Template


def add_spaces(text):
    return " ".join(text)


def discipline(number):
    remainder = number % 10
    if remainder in [0, 5, 6, 7, 8, 9] or number in [11, 12, 13, 14]:
        return "дисциплин"
    elif remainder in [2, 3, 4]:
        return "дисциплины"
    elif remainder in [1]:
        return "дисциплина"


student = [
    ["Алина", "Бизнес-информатика", ["Базы данных",
                                     "Программирование", "Эконометрика", "Статистика"], "ж"],
    ["Вадим", "Экономика", ["Информатика", "Теория игр",
                            "Экономика", "Эконометрика", "Статистика"], "м"],
    ["Ксения", "Экономика", ["Информатика", "Теория игр",
                             "Статистика"], "ж"]
]

f_template = open('test_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
template.globals["add_spaces"] = add_spaces
template.globals["len"] = len
result_html = template.render(user=student[2])

# создадим файл для HTML-страницы
f = open('test.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()

# Самостоятельная работа
f_template = open('ind_test_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
template.globals["discipline"] = discipline
template.globals["add_spaces"] = add_spaces
template.globals["len"] = len
result_html = template.render(user=student[2])

# создадим файл для HTML-страницы
f = open('ind_test.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
