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
    

# Insert new movie in the register and add or delete in the inventary

# Add a new client
def add_rent():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()
    id_pelicula = data['id_pelicula']
    id_cliente = data['id_cliente']
    id_empleado = data['id_empleado']
    fecha_devolucion = data['fecha_devolucion']
    id_pago = data['id_pago']


    cur.execute('INSERT INTO alquiler (id_pelicula, id_cliente, fecha_alquiler, id_empleado, fecha_devolucion, id_pago) VALUES (%s, %s, CURDATE(), %s, %s, %s)', (id_pelicula, id_cliente, id_empleado, fecha_devolucion, id_pago))
    conn.commit()
    conn.close()
    restar_cantidad_inventario(id_pelicula)
    print('Registro agregada')
    return "Registro agregado"     


def restar_cantidad_inventario(id_pelicula):
    conn = connectdb()
    cur = conn.cursor()

    # Restar uno a la cantidad del inventario de la película
    cur.execute("UPDATE inventario SET cantidad = cantidad - 1 WHERE id_pelicula = %s", (id_pelicula,))
    conn.commit()

    conn.close()




#get all in rent table
def obtener_info_todas_alquiler():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('select * from alquiler')
    dato_alquiler = cur.fetchall()
    print("dato_alquiler")
    if dato_alquiler:
        data = [{'id_pelicula': dato[1], 'id_cliente': dato[2], 'fecha_alquiler': dato[3], 'id_empleado': dato[4], 'fecha_devolucion': dato[5],'id_pago': dato[6]} for dato in dato_alquiler]
        conn.close()
        return jsonify(data)
    else:
        return 'The movies was not found'  

#Return movie by id EN PROGRESS
# def return_movie(id_alquiler):
#     conn = connectdb()
#     cur = conn.cursor()

#     data = request.get_json()

#     if "fecha_devolucion" in data:
#         fecha_devolucion = data["fecha_devolucion"]
#         cur.execute('UPDATE alquiler SET fecha_devolucion = CURDATE() WHERE id_alquiler = %s', (fecha_devolucion, id_alquiler))

#     conn.commit()
#     conn.close()

#     return 'Register updated'

# Returning movie
def return_movie(id_alquiler):
    conn = connectdb()
    cur = conn.cursor()

    data = request.get_json()
    id_pelicula = data.get('id_pelicula')
    new_fecha_devolucion = data.get('fecha_devolucion')

    cur.execute('UPDATE alquiler SET fecha_devolucion = %s WHERE id_alquiler = %s', (new_fecha_devolucion, id_alquiler))
    conn.commit()
    conn.close()
    increase_cantidad_inventario(id_pelicula)
    return 'Fecha de devolución actualizada'

#D
def increase_cantidad_inventario(id_pelicula):
    conn = connectdb()
    cur = conn.cursor()

    # Restar uno a la cantidad del inventario de la película
    cur.execute("UPDATE inventario SET cantidad = cantidad + 1 WHERE id_pelicula = %s", (id_pelicula,))
    conn.commit()

    conn.close()