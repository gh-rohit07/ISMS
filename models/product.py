from extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    expiry_date = db.Column(db.Date, nullable=True)
    min_reorder_level = db.Column(db.Integer, default=10)
    transactions = db.relationship('Transaction', backref='product', lazy=True, cascade="all, delete-orphan")
