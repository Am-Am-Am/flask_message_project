from flask import Flask, render_template, request
import pymorphy2
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        morph = pymorphy2.MorphAnalyzer()
        name = request.form.get('name')
        date = request.form.get('date')
        welcome = ''
        name = morph.parse(name)[0]
        correct_name = name.inflect({'ablt'})
        current_time = datetime.datetime.now().time()

        if current_time > datetime.time(1, 0) and current_time < datetime.time(9, 0):
            welcome = 'Доброе утро!'
        elif current_time >= datetime.time(9, 0) and current_time < datetime.time(13, 0):
            welcome = 'Добрый день!'
        else:
            welcome = 'Добрый вечер!'

        message = f'{welcome} Меня зовут Амур, я преподаватель из школы программирования Kodland. Нам с {correct_name.word.capitalize()} назначили дополнительный экспертный урок для определения дальнейшего курса обучения. Время проведения: {date}.'

        return render_template('index.html', message=message)
    else:
        return render_template('index.html')




# app.run()