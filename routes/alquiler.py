from flask import jsonify, request
from database.db import connectdb

# Obtain all information by tittle

def obtener_info_por_titulo(titulo):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute(
        """SELECT p.id_pelicula, p.titulo, p.año, p.director, p.categoria, p.precio, i.cantidad
        FROM peliculas p
        JOIN inventario i ON p.id_pelicula = i.id_pelicula
        WHERE p.titulo = %s""",
        (titulo,)
    )
    dato_pelicula = cur.fetchone()
    print("dato_pelicula")
    if dato_pelicula:
        dato = {
            'id_pelicula': dato_pelicula[0],
            'titulo': dato_pelicula[1],
            'año': dato_pelicula[2],
            'director': dato_pelicula[3],
            'categoria': dato_pelicula[4],
            'precio': dato_pelicula[5],
            'cantidad': dato_pelicula[6]
        }
        conn.close()
        return jsonify(dato)
    else:
        return 'The movie was not found'

    
# Obtain all information in the inventary
    
def obtener_info_todas_peliculas():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute(
    """SELECT p.id_pelicula, p.titulo, p.año, p.director, p.categoria, p.precio, i.cantidad
    FROM peliculas p
    JOIN inventario i ON p.id_pelicula = i.id_pelicula
    WHERE p.id_pelicula = i.id_pelicula """)
    dato_pelicula = cur.fetchall()
    print("dato_cliente")
    if dato_pelicula:
        data = [{'id_pelicula': dato[0], 'titulo': dato[1], 'año': dato[2], 'director': dato[3], 'categoria': dato[4],'precio': dato[5], 'cantidad': dato[6]} for dato in dato_pelicula]
        conn.close()
        return jsonify(data)
    else:
        return 'The movies was not found'    