from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ryn'}
    posts = [
        {
            'author': {'username': 'Basil'},
            'body': 'I woke up today and chose violence.'
        },
        {
            'author': {'username': 'Violet'},
            'body': 'Ball? Ball. Ball. Play? Ball. Ball?'
        },
        {
            'author': {'username': 'Ollie', 'species': 'human'},
            'body': 'Oh no!'
        }
    ]
    return render_template('index.html', title='Meow', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
