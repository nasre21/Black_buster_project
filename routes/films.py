from flask import jsonify, request, render_template, redirect
from database.db import connectdb


def add_movie():
    conn = connectdb()
    cur = conn.cursor()
    
    titulo = request.form['titulo']
    año = request.form['año']
    director = request.form['director']
    categoria = request.form['categoria']
    precio = request.form['precio']
    
    cur.execute('INSERT INTO peliculas (titulo, año, director, categoria, precio) VALUES (%s, %s, %s,%s, %s)',(titulo, año, director, categoria, precio))
    
    conn.commit()
    conn.close()
    print('films created')
    return redirect("/movies")

def get_movie():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM peliculas')
    datos_peliculas = cur.fetchall()
    data = [{'id_pelicula': dato[0], 'titulo': dato[1], 'año': dato[2], 'director': dato[3], 'categoria': dato[4],'precio': dato[5]} for dato in datos_peliculas]
    conn.close()
    return render_template('dashboard.html', data=data)
 


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

def del_movie(id_pelicula):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('DELETE FROM peliculas WHERE id_pelicula= %s', (id_pelicula,))
    conn.commit()
    conn.close()
    print("pelicula eliminada !!")
    
    return redirect("/movies")


def update_pelicula(id_pelicula):
    conn = connectdb()
    cur = conn.cursor()

    data = request.get_json()

    if "titulo" in data:
        titulo = data["titulo"]
        cur.execute('UPDATE peliculas SET titulo = %s WHERE id_pelicula = %s', (titulo, id_pelicula))

    if "año" in data:
        año = data["año"]
        cur.execute('UPDATE peliculas SET año = %s WHERE id_pelicula = %s', (año, id_pelicula))

    if "director" in data:
        director = data["director"]
        cur.execute('UPDATE peliculas SET director= %s WHERE id_pelicula = %s', (director, id_pelicula))
        
    if "categoria" in data:
        categoria = data["categoria"]
        cur.execute('UPDATE peliculas SET categoria= %s WHERE id_pelicula = %s', (categoria, id_pelicula))
        
        
    if "precio" in data:
        precio = data["precio"]
        cur.execute('UPDATE peliculas SET precio= %s WHERE id_pelicula = %s', (precio, id_pelicula))    
        
        

    conn.commit()
    conn.close()

    return 'Dato modificado'


    
def max_peliculas():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM peliculas WHERE precio = (SELECT MAX(precio) FROM peliculas)')
    dato_movie = cur.fetchone()
    respuesta = {
        "id":dato_movie[0],
        "titulo": dato_movie[1],
        "year":dato_movie[2],
         "director": dato_movie[3],
        "categoria": dato_movie[4],
        "precio":dato_movie[5], 
    }
    conn.close()
    print("pelicula eliminada !!")
    return jsonify(respuesta, 200)

def min_peliculas():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM peliculas WHERE precio = (SELECT MIN(precio) FROM peliculas)')
    dato_movie = cur.fetchone()
    respuesta = {
        "id":dato_movie[0],
        "titulo": dato_movie[1],
        "year":dato_movie[2],
         "director": dato_movie[3],
        "categoria": dato_movie[4],
        "precio":dato_movie[5], 
    }
    conn.close()
    print("pelicula eliminada !!")
    return jsonify(respuesta, 200)

 
 
def categoria_peliculas():
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("SELECT categoria FROM peliculas")
    dato_movie = cursor.fetchall()
    print(dato_movie)
    return dato_movie
 
def director_peliculas():
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("SELECT director FROM peliculas")
    dato_movie = cursor.fetchall()
    print(dato_movie)
    return dato_movie

def año_peliculas():
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("SELECT año FROM peliculas")
    dato_movie = cursor.fetchall()
    print(dato_movie)
    return dato_movie

 
 
 