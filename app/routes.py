from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nikita'}
    posts = [
        {
            'author': {'username': 'Виктор'},
            'body': 'Сообщение Виктора'
        },
        {
            'author': {'username': 'Петр'},
            'body': 'Сообщнеие Петра'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
