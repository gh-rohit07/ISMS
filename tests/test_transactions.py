def test_transaction_flow(client, auth):
    auth.login()
    # Create a product
    client.post('/products/new', data={
        'name': 'Stock Item',
        'category': 'General',
        'price': '10',
        'supplier': 'S1',
        'min_reorder_level': '5',
        'expiry_date': ''
    })
    
    # Transaction IN
    client.post('/transactions/new', data={
        'product_id': '1',
        'type': 'IN',
        'quantity': '100'
    }, follow_redirects=True)
    
    # Verify stock in reports
    response = client.get('/reports')
    assert b'100' in response.data
    
    # Transaction OUT
    client.post('/transactions/new', data={
        'product_id': '1',
        'type': 'OUT',
        'quantity': '30'
    }, follow_redirects=True)
    
    # Verify remaining stock
    response = client.get('/reports')
    assert b'70' in response.data

def test_insufficient_stock(client, auth):
    auth.login()
    client.post('/products/new', data={
        'name': 'Limited Item',
        'category': 'General',
        'price': '10',
        'supplier': 'S1',
        'min_reorder_level': '5',
        'expiry_date': ''
    })
    
    response = client.post('/transactions/new', data={
        'product_id': '1',
        'type': 'OUT',
        'quantity': '10'
    }, follow_redirects=True)
    
    assert b'Insufficient stock' in response.data
