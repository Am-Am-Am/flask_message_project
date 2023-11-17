from flask import Flask, render_template, request 
import pymorphy2

app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        morph = pymorphy2.MorphAnalyzer()
        name = request.form.get('name')
        date = request.form.get('date')
        welcome = request.form.get('welcome')
        name = morph.parse(name)[0]

        correct_name = name.inflect({'ablt'})

        if welcome == '1':
            welcome = 'Доброе утро!'
        elif welcome == '2':
            welcome = 'Добрый день!'
        elif welcome == '3':
            welcome = 'Добрый вечер!'
        message = f'{welcome} Меня зовут Амур, я преподаватель из школы программирования Kodland. Нам с {correct_name.word.capitalize()} назначили дополнительный урок для определения дальнейшего курса обучения. Время проведения: {date}.'

        return render_template('index.html', message=message)
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html')




app.run()