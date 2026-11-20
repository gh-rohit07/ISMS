from flask import Blueprint, render_template
from flask_login import login_required
from models import Product, Transaction
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def dashboard():
    products_count = Product.query.count()
    low_stock_products = Product.query.filter(Product.quantity <= Product.min_reorder_level).all()
    
    from datetime import date, timedelta
    today = date.today()
    thirty_days_later = today + timedelta(days=30)
    expiring_soon = Product.query.filter(Product.expiry_date.between(today, thirty_days_later)).all()
    
    total_inventory_value = db.session.query(db.func.sum(Product.price * Product.quantity)).scalar() or 0
    
    recent_transactions = Transaction.query.order_by(Transaction.date.desc()).limit(5).all()
    
    return render_template('dashboard.html', 
                           products_count=products_count,
                           low_stock_products=low_stock_products,
                           expiring_soon=expiring_soon,
                           total_inventory_value=total_inventory_value,
                           recent_transactions=recent_transactions)
