import pytest
from flask import Flask
from routes.empleados import *

@pytest.fixture
def client():
    app = Flask(__name__)
    app.testing = True
    app.route('/add_empleado', methods=['POST'])(add_empleado)
    app.route('/get_empleados', methods=['GET'])(get_empleados)
    app.route('/obtener_empleado/<int:id_empleado>')(obtener_empleado_por_id)
    app.route('/empleados_del/<int:id_empleado>', methods=['DELETE'])(del_empleado)
    app.route("/update_empleado/<int:id_empleado>", methods=["PUT"])(update_empleado)

    client = app.test_client()
    yield client

def test_add_empleado(client):
    response = client.post('/add_empleado', json={'nombre': 'John', 'apellido': 'Doe', 'cargo': 'Developer'})
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Empleado agregado'

def test_get_empleados(client):
    response = client.get('/get_empleados')
    assert response.status_code == 200
    # Verificar la estructura y los datos de la respuesta JSON
    data = response.get_json()
    assert isinstance(data, list)
    if len(data) > 0:
        empleado = data[0]
        assert 'id_empleado' in empleado
        assert 'empleados' in empleado
        assert 'cargo' in empleado

def test_obtener_empleado_por_id(client):
    response = client.get('/obtener_empleado/36')
    assert response.status_code == 200
    # Verificar la estructura y los datos de la respuesta JSON
    data = response.get_json()
    assert 'id_empleado' in data
    assert 'empleados' in data
    assert 'cargo' in data

def test_del_empleado(client):
    response = client.delete('/empleados_del/37')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Empleado eliminado !!'

def test_update_empleado(client):
    response = client.put('/update_empleado/1', json={'nombre': 'John'})
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Dato modificado'
