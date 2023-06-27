import pytest
from app import app
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@patch('routes.empleados.connectdb')
def test_add_empleado(mock_connectdb, client):
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_connectdb.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur

    data = {
        'nombre': 'Anyell',
        'apellido': 'Mendoza',
        'cargo': 'Admin'
    }

    response = client.post('/empleado_add', json=data)

    assert response.status_code == 200

    mock_connectdb.assert_called_once()
    mock_conn.cursor.assert_called_once()
    mock_cur.execute.assert_called_once_with(
        'INSERT INTO empleados (nombre, apellido, cargo) VALUES (%s, %s, %s)',
        ('Anyell', 'Mendoza', 'Admin')
    )
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()



    assert response.get_data(as_text=True) == 'Empleado agregado'