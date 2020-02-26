def test_new_user(test_client):

    new_user = {
        'username': 'johndoe',
        'email': 'john@doe.com',
        'image_url': 'https://dummyimage.com/629x296'
    }

    response = test_client.post(
        '/v1/user',
        json=new_user,
        content_type='application/json'
    )
    assert response.status_code == 200
