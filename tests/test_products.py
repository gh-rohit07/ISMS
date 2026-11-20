def test_create_product(client, auth):
    auth.login()
    response = client.post('/products/new', data={
        'name': 'Test Product',
        'category': 'Electronics',
        'price': '99.99',
        'supplier': 'Test Supplier',
        'min_reorder_level': '5',
        'expiry_date': '2026-12-31'
    }, follow_redirects=True)
    assert b'Test Product' in response.data

def test_edit_product(client, auth, app):
    auth.login()
    client.post('/products/new', data={
        'name': 'Old Name',
        'category': 'Electronics',
        'price': '10',
        'supplier': 'Supplier',
        'min_reorder_level': '1',
        'expiry_date': ''
    })
    
    response = client.post('/products/edit/1', data={
        'name': 'New Name',
        'category': 'Electronics',
        'price': '15',
        'supplier': 'Supplier',
        'min_reorder_level': '1',
        'expiry_date': ''
    }, follow_redirects=True)
    assert b'New Name' in response.data
    assert b'Old Name' not in response.data

def test_unauthorized_product_creation(client, auth):
    auth.login('staff', 'staff123')
    response = client.get('/products/new')
    assert response.status_code == 403
