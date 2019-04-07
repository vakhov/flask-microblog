from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Alexander'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'boyd': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'boyd': 'The Avengers movie was so cool!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
