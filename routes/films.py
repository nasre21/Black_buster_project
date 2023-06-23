from flask import jsonify, request
from database.db import connectdb


def add_movie():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()
    
    titulo = data['titulo']
    año = data['año']
    director = data['director']
    categoria = data['categoria']
    precio = data['precio']
    
    
    cur.execute('INSERT INTO peliculas (titulo, año, director, categoria, precio) VALUES (%s, %s, %s,%s, %s)',(titulo, año, director, categoria, precio))
    
    conn.commit()
    conn.close()
    print('films created')
    return "Films add"

def get_movie():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM peliculas')
    datos_peliculas = cur.fetchall()
    data = [{'id_pelicula': dato[0], 'titulo': dato[1], 'año': dato[2], 'director': dato[3], 'categoria': dato[4],'precio': dato[5]} for dato in datos_peliculas]
    conn.close()
    return jsonify(data)


def get_one(id_pelicula):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM peliculas WHERE id_pelicula = %s', (id_pelicula,))
    dato_movie = cur.fetchone()
    print("dato_movie")

    if dato_movie:
        dato = {'id_pelicula': dato_movie[0], 'titulo': dato_movie[1], 'año': dato_movie[2],'director': dato_movie[3],'categoria': dato_movie[4],'precio': dato_movie[5]}
        conn.close()
        return jsonify(dato)
    else:
        return 'pelicula no encontrado'
