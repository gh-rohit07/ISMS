from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import Product, Transaction
from extensions import db

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions')
@login_required
def index():
    all_transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    return render_template('transactions/index.html', transactions=all_transactions)

@transactions_bp.route('/transactions/new', methods=['GET', 'POST'])
@login_required
def new_transaction():
    all_products = Product.query.all()
    if request.method == 'POST':
        product_id = int(request.form.get('product_id'))
        tx_type = request.form.get('type')
        quantity = int(request.form.get('quantity'))
        
        product = Product.query.get_or_404(product_id)
        
        if tx_type == 'OUT' and product.quantity < quantity:
            flash('Insufficient stock')
            return render_template('transactions/form.html', products=all_products)
        
        if tx_type == 'IN':
            product.quantity += quantity
        else:
            product.quantity -= quantity
            
        tx = Transaction(product_id=product_id, type=tx_type, quantity=quantity, user_id=current_user.id)
        db.session.add(tx)
        db.session.commit()
        return redirect(url_for('transactions.index'))
    return render_template('transactions/form.html', products=all_products)
