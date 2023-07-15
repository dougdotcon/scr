from flask import Blueprint, render_template, request
from flask_paginate import Pagination
from flask_login import login_required, current_user
from models import Product  # ou de onde você importa a classe Product

bp = Blueprint('main', __name__)

@bp.route('/')
def dashboard():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    products = Product.query.paginate(page, per_page)
    pagination = Pagination(page=page, total=products.total, per_page=per_page)
    return render_template('dashboard.html', products=products, pagination=pagination)

@bp.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role == 'admin':
        return render_template('admin_dashboard.html')
    else:
        return 'Acesso não autorizado'