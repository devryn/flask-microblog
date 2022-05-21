from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
#make this a protected function
def index():
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
    return render_template('index.html', title='Meow', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #if user is already logged in redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    #new login form instance    
    form = LoginForm()
    #login if validated
    if form.validate_on_submit():
        #load user from db
        user = User.query.filter_by(username=form.username.data).first()
        #do pw hashes match?
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))