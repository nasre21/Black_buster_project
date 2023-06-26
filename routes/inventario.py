from flask import jsonify, request
from database.db import connectdb

def get_inventario():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM inventario')
    datos_peliculas = cur.fetchall()
    data = [{'id':dato[0],'id_pelicula': dato[1], 'cantidad': dato[2]} for dato in datos_peliculas]
    conn.close()
    return jsonify(data)

def get_one_inventario(id_pelicula):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM inventario WHERE id = %s',(id_pelicula,))
    datos_peliculas = cur.fetchone()
    if datos_peliculas:
       data = {'id':datos_peliculas[0],'id_pelicula': datos_peliculas[1], 'cantidad': datos_peliculas[2]}
       conn.close()
       return jsonify(data)
    else:
       return 'The client was not found'