@route('/api-request')
def returnarray():
    rv = [{ "id": 1, "name": "Test Item 1" }, { "id": 2, "name": "Test Item 2" }]
    return dict(data=rv)

application = default_app()
