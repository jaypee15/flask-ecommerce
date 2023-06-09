from flask import (
    Blueprint,redirect, render_template, request,url_for, flash 
)
from flask_login import login_user, logout_user, login_required
bp = Blueprint('auth', __name__, url_prefix='/auth')
from jstore.forms import RegisterForm, LoginForm
from jstore.models import User, Item
from jstore.extensions import db

@bp.route('/register', methods=('GET', 'POST'))
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
        return redirect(url_for('market.market_page'))
        #check if there are validation errors
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f'Error while creating user: {err_msg}', category='danger')

    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market.market_page'))
        else:
            flash('Username and password do not match! Please try again', category='danger')

    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
