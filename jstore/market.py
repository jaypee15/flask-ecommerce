from flask import (
    Blueprint,redirect, render_template, request, 
)
from werkzeug.exceptions import abort
from jstore.extensions import db
from jstore.models import Item
from flask_login import  login_required, logout_user


bp = Blueprint('market', __name__)


@bp.route('/')
@bp.route('/home')
def index():
    return render_template('market/index.html')

@bp.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market/market.html', items=items) 

@bp.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("index"))





