from flask import jsonify, request
from database.db import connectdb

def get_inventario():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM inventario')
    datos_clientes = cur.fetchall()
    data = [{'id_pelicula': dato[1], 'cantidad': dato[2]} for dato in datos_clientes]
    conn.close()
    return jsonify(data)