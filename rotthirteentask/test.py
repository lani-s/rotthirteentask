from webtest import TestApp
from main import application

app = TestApp(application())

def test_index():
    response = app.get('/')
    assert 'Hello world!' in str(response)