from flask import Flask, render_template
from extensions import db, login_manager
from models import User
from werkzeug.security import generate_password_hash
import os

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'isms-flask-secret-key-2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if test_config:
        app.config.update(test_config)
    
    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register Blueprints
    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.products import products_bp
    from routes.transactions import transactions_bp
    from routes.reports import reports_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(reports_bp)
    
    @app.errorhandler(403)
    def unauthorized(e):
        return render_template('error.html', message="Unauthorized access"), 403

    # Create admin user if it doesn't exist (skip in testing)
    if not app.config.get('TESTING'):
        with app.app_context():
            db.create_all()
            if not User.query.filter_by(username='admin').first():
                admin = User(username='admin', password=generate_password_hash('admin123'), role='Admin')
                db.session.add(admin)
                db.session.commit()
            
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=3000)
