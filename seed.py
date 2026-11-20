from app import create_app
from extensions import db
from models import User, Product, Transaction
from werkzeug.security import generate_password_hash
from datetime import date, timedelta, datetime
import random

def seed_data():
    app = create_app()
    with app.app_context():
        # Clear existing data to avoid duplicates (optional, but good for a clean seed)
        db.drop_all()
        db.create_all()

        print("Seeding users...")
        users_data = [
            ("Alice Johnson", "alice_admin", "Admin"),
            ("Robert Smith", "bob_manager", "Manager"),
            ("Charlie Davis", "charlie_staff", "Staff"),
            ("Diana Prince", "diana_staff", "Staff")
        ]
        
        users = []
        password_hash = generate_password_hash("password123")
        for name, username, role in users_data:
            user = User(username=username, password=password_hash, role=role)
            db.session.add(user)
            users.append(user)
        
        # Ensure the default 'admin' exists too
        if not User.query.filter_by(username='admin').first():
            db.session.add(User(username='admin', password=generate_password_hash('admin123'), role='Admin'))

        db.session.commit()

        print("Seeding products...")
        products_data = [
            ("MacBook Pro 14\"", "Electronics", 1999.99, "Apple Inc.", 5, date.today() + timedelta(days=730)),
            ("iPhone 15 Pro", "Electronics", 1099.00, "Apple Inc.", 10, date.today() + timedelta(days=365)),
            ("Dell UltraSharp 27", "Electronics", 549.50, "Dell", 3, None),
            ("Logitech MX Master 3S", "Accessories", 99.00, "Logitech", 15, None),
            ("Keychron K2 Keyboard", "Accessories", 79.00, "Keychron", 10, None),
            ("Sony WH-1000XM5", "Audio", 399.99, "Sony", 8, date.today() + timedelta(days=500)),
            ("Bose QuietComfort", "Audio", 349.00, "Bose", 5, None),
            ("Standing Desk", "Furniture", 450.00, "Fully", 2, None),
            ("Herman Miller Aeron", "Furniture", 1200.00, "Herman Miller", 2, None),
            ("USB-C Hub", "Accessories", 45.00, "Anker", 20, None),
            ("Monitor Arm", "Accessories", 80.00, "Ergotron", 5, None),
            ("Milk Carton 1L", "Groceries", 2.50, "Local Dairy", 50, date.today() + timedelta(days=5)), # Expiring soon
            ("Bread Loaf", "Groceries", 3.00, "Bakery", 40, date.today() + timedelta(days=2)), # Expiring very soon
        ]

        products = []
        for name, cat, price, supplier, min_level, expiry in products_data:
            # Set initial quantity to something realistic or let transactions handle it
            qty = random.randint(0, 30)
            product = Product(
                name=name, 
                category=cat, 
                price=price, 
                quantity=qty,
                supplier=supplier, 
                min_reorder_level=min_level, 
                expiry_date=expiry
            )
            db.session.add(product)
            products.append(product)
        
        db.session.commit()

        print("Seeding transactions...")
        # Create some history
        for _ in range(20):
            product = random.choice(products)
            user = random.choice(users)
            tx_type = random.choice(["IN", "OUT"])
            qty = random.randint(1, 5)
            
            # Adjust product quantity to match transaction logic if needed
            # For seeding, we'll just record the transaction
            tx = Transaction(
                product_id=product.id,
                type=tx_type,
                quantity=qty,
                user_id=user.id,
                date=datetime.utcnow() - timedelta(days=random.randint(0, 10))
            )
            db.session.add(tx)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
