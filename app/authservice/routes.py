from flask import render_template, redirect, url_for, flash
from app.authservice import auth_bp
from app.authservice.forms import LoginForm, SignupForm
from flask_login import login_user, logout_user, current_user
from app import db
from app.authservice.models import User

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = SignupForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

        # Create a new user and hash the password
        user = User(username=form.username.data)
        user.set_password(form.password.data)  # Hashing happens here

        print(user.username)
        print(user.password_hash)  # This should print a hashed password

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('authservice.login'))
    
    return render_template('signup.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out!', 'info')
    return redirect(url_for('authservice.login'))
