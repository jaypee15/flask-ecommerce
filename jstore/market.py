from flask import (
    Blueprint,redirect, render_template, request, 
)
from werkzeug.exceptions import abort
from jstore.extensions import db
from jstore.models import Item



bp = Blueprint('market', __name__)


@bp.route('/')
@bp.route('/home')
def index():
    return render_template('market/index.html')

@bp.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market/market.html', items=items) 





