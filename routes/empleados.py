from flask import jsonify, request, make_response
from database.db import connectdb

def add_empleado():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()

    nombre = data['nombre']
    apellido = data['apellido']
    cargo = data['cargo']

    cur.execute('INSERT INTO empleados (nombre, apellido, cargo) VALUES (%s, %s, %s)', (nombre, apellido, cargo))
    conn.commit()
    conn.close()
    print('Empleado creado')
    return "Empleado agregado"

from flask import make_response, jsonify

def get_empleados():
    conn = connectdb()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM empleados')
        datos_empleados = cur.fetchall()
        data = [{'id_empleado': dato[0], 'empleados': dato[1], 'cargo': dato[3]} for dato in datos_empleados]
        conn.close()

        response = make_response(jsonify(data))
        response.status_code = 200  # Código de estado 200 (OK)
    except:
        # Manejo de errores en caso de fallo en la consulta o conexión a la base de datos
        conn.close()
        response = make_response("Error en la consulta a la base de datos", 500)  # Código de estado 500 (Internal Server Error)

    return response


def obtener_empleado_por_id(id_empleado):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM empleados WHERE id_empleado = %s', (id_empleado,))
    dato_empleado = cur.fetchone()

    if dato_empleado:
        dato = {'id_empleado': dato_empleado[0], 'empleados': dato_empleado[1], 'cargo': dato_empleado[3]}
        conn.close()
        return jsonify(dato)
    else:
        return 'Empleado no encontrado'

def del_empleado(id_empleado):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('DELETE FROM empleados WHERE id_empleado = %s', (id_empleado,))
    conn.commit()
    conn.close()
    print("Empleado eliminado !!")
    return "Empleado eliminado !!"

def update_empleado(id_empleado):
    conn = connectdb()
    cur = conn.cursor()

    data = request.get_json()

    if "nombre" in data:
        nombre = data["nombre"]
        cur.execute('UPDATE empleados SET nombre = %s WHERE id_empleado = %s', (nombre, id_empleado))

    if "apellido" in data:
        apellido = data["apellido"]
        cur.execute('UPDATE empleados SET apellido = %s WHERE id_empleado = %s', (apellido, id_empleado))

    if "cargo" in data:
        cargo = data["cargo"]
        cur.execute('UPDATE empleados SET cargo = %s WHERE id_empleado = %s', (cargo, id_empleado))

    conn.commit()
    conn.close()

    return 'Dato modificado'
