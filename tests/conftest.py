import pytest
from app import create_app
from extensions import db
from models import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'WTF_CSRF_ENABLED': False
    })

    with app.app_context():
        db.create_all()
        # Create users for testing
        admin = User(username='admin', password=generate_password_hash('admin123'), role='Admin')
        manager = User(username='manager', password=generate_password_hash('manager123'), role='Manager')
        staff = User(username='staff', password=generate_password_hash('staff123'), role='Staff')
        db.session.add_all([admin, manager, staff])
        db.session.commit()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth(client):
    class AuthActions:
        def login(self, username='admin', password='admin123'):
            return client.post('/login', data={'username': username, 'password': password}, follow_redirects=True)
        
        def logout(self):
            return client.get('/logout', follow_redirects=True)
            
    return AuthActions()
