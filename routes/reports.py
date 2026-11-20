from flask import Blueprint, render_template
from flask_login import login_required
from models import Product
from extensions import db
from .utils import role_required
from datetime import date

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/reports')
@login_required
@role_required(['Admin', 'Manager'])
def index():
    all_products = Product.query.all()
    total_value = sum(p.price * p.quantity for p in all_products)
    
    # Category breakdown
    category_data = db.session.query(
        Product.category, 
        db.func.count(Product.id), 
        db.func.sum(Product.price * Product.quantity)
    ).group_by(Product.category).all()
    
    today = date.today()
    
    return render_template('reports/index.html', 
                           products=all_products, 
                           total_value=total_value, 
                           category_breakdown=category_data,
                           today=today)
