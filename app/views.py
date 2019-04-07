from flask import flash
from flask import redirect
from flask import render_template
from app import app
from .forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login required for OpenID={0}, remember_me={1}'.format(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
