def test_login_logout(client, auth):
    # Test login
    response = auth.login()
    assert b'Total Products' in response.data
    
    # Test logout
    response = auth.logout()
    assert b'LOGIN' in response.data

def test_invalid_login(client, auth):
    response = auth.login('admin', 'wrongpass')
    assert b'Invalid username or password' in response.data
