import pytest
from flask import Flask
from routes.films import *

@pytest.fixture
def client():
    app = Flask(__name__)
    app.testing = True
    app.route('/movies_add', methods =['POST'])(add_movie)
    app.route('/movies', methods =['GET'])(get_movie)
    app.route('/movies/<int:id_pelicula>', methods=['GET'])(get_one)
    app.route('/movies_del/<int:id_pelicula>', methods=['DELETE'])(del_movie)
    app.route("/movies/<int:id_pelicula>", methods=["PATCH"])(update_pelicula) 
    
    
    client = app.test_client()
    yield client 

def test_add_movies(client):
    response = client.post('/movies_add', json = {'titulo':'9 reinas','año':1998,'director':'fabian beilinsky','categoria':'drama','precio':14})
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Films add'
    
def test_get_empleado(client):
   response = client.get('/movies')
   assert response.status_code == 200
    # Verificar la estructura y los datos de la respuesta JSON
   data = response.get_json()
   assert isinstance(data, list)
   if len(data) > 0:
        movies = data[0]
        assert 'id_pelicula' in movies
        assert 'titulo' in movies
        assert 'año' in movies
        assert 'director' in movies
        assert 'categoria' in movies
        assert 'precio' in movies
        
        

def test_obtener_movie_por_id(client):
    response = client.get('/movies/3')
    assert response.status_code == 200
    # Verificar la estructura y los datos de la respuesta JSON
    movies = response.get_json()
    assert 'id_pelicula' in movies
    assert 'titulo' in movies
    assert 'año' in movies
    assert 'director' in movies
    assert 'categoria' in movies
    assert 'precio' in movies
    
    
def test_del_movie(client):
    response = client.delete('/movies_del/2')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'removed movie !!'
    # 
def test_update_movies(client):
    response = client.patch('/movies/5', json={'id_peliculas':3,'titulo':'el padrino','año':2005, 'direccion':'Francis Ford Coppola','categoria':'drama', 'precio':10})
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Dato modificado' 
