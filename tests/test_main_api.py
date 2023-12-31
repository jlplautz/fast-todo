from fastapi import status
from fastapi.testclient import TestClient

from todo.app import app

client = TestClient(app)


def test_main_api_works_ok():
    """This test guartantees that the endpoint works propely."""
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.text == '{"message":"Hello, World!!!"}'


def test_main_api_has_docs():
    """This test guarantees that this API has a documentation."""
    response = client.get('/docs')
    assert response.status_code == status.HTTP_200_OK
