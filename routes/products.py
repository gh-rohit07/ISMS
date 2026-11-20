from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models import Product
from extensions import db
from .utils import role_required
from datetime import datetime

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
@login_required
def index():
    all_products = Product.query.all()
    return render_template('products/index.html', products=all_products)

@products_bp.route('/products/new', methods=['GET', 'POST'])
@login_required
@role_required(['Admin', 'Manager'])
def new_product():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        price = float(request.form.get('price'))
        supplier = request.form.get('supplier')
        min_reorder_level = int(request.form.get('min_reorder_level'))
        expiry_date_str = request.form.get('expiry_date')
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date() if expiry_date_str else None

        product = Product(name=name, category=category, price=price, supplier=supplier, 
                          min_reorder_level=min_reorder_level, expiry_date=expiry_date)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products.index'))
    return render_template('products/form.html', product=None)

@products_bp.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required(['Admin', 'Manager'])
def edit_product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.category = request.form.get('category')
        product.price = float(request.form.get('price'))
        product.supplier = request.form.get('supplier')
        product.min_reorder_level = int(request.form.get('min_reorder_level'))
        expiry_date_str = request.form.get('expiry_date')
        product.expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date() if expiry_date_str else None
        
        db.session.commit()
        return redirect(url_for('products.index'))
    return render_template('products/form.html', product=product)

@products_bp.route('/products/delete/<int:id>', methods=['POST'])
@login_required
@role_required(['Admin'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.index'))
