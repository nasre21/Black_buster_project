import pytest
from flask import Flask
from routes.pagos import *

@pytest.fixture
def client():
    app = Flask(__name__)
    app.testing = True
    app.route("/pagos", methods=["GET"])(get_payments)
    
    client = app.test_client()
    yield client 
    
def test_get_pagos(client):
    response = client.get("/pagos")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    if len(data) > 0:
        pagos = data[0]
        assert 'id_pago' in pagos
        assert 'monto' in pagos
        assert 'fecha_pago' in pagos
        assert 'metodo' in pagos