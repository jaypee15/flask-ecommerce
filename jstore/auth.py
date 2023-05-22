from flask import (
    Blueprint,redirect, render_template, request,url_for, flash 
)
bp = Blueprint('auth', __name__, url_prefix='/auth')
from jstore.forms import RegisterForm
from jstore.models import User
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
            flash(f'Error while creating user: {err_msg}')

    return render_template('auth/register.html', form=form)