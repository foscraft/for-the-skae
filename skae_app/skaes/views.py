from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user,login_user,logout_user
from .models import User
from .forms import LoginForm, SignupForm, EditAccountForm
#from skaes.decorators import admin_required
#from skaes.extensions import db

skaes = Blueprint('skaes', __name__)
@skaes.route('/')
def index():
    return render_template('index.html')

@skaes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('skaes.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('skaes.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('skaes.index'))
    return render_template('login.html', form=form)

@skaes.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('skaes.index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
             username=form.username.data,
             bio=form.bio.data, 
             email=form.email.data
             )
        user.set_password(form.password.data)
        User.session.add(user)
        User.session.commit()
        return redirect(url_for('skaes.login'))
    return render_template('signup.html', form=form)

@skaes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('skaes.index'))

@skaes.route('/editaccount', methods=['GET', 'POST'])
@login_required
def editaccount():
    form = EditAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.bio = form.bio.data
        current_user.email = form.email.data
        User.session.commit()
        return redirect(url_for('skaes.index'))
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.username.data = current_user.username
    form.bio.data = current_user.bio
    form.email.data = current_user.email
    return render_template('editaccount.html', form=form)