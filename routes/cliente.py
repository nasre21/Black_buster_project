from flask import jsonify, request
from database.db import connectdb

# Add a new client
def add_cliente():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()

    nombre = data['nombre']
    apellidos = data['apellidos']
    edad = data['edad']
    telefono = data['telefono']
    direccion = data['direccion']
    email = data['email']


    cur.execute('INSERT INTO clientes (nombre, apellidos, edad, telefono, direccion, email) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellidos, edad, telefono, direccion, email))
    conn.commit()
    conn.close()
    print('Empleado creado')
    return "Empleado agregado"

# Obtain a new client

def get_clientes():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clientes')
    datos_clientes = cur.fetchall()
    data = [{'id_cliente': dato[0], 'nombre': dato[1], 'apellidos': dato[2], 'edad': dato[3], 'telefono': dato[4],'direccion': dato[5], 'email': dato[6]} for dato in datos_clientes]
    conn.close()
    return jsonify(data)

# Obtain a client by id

def obtener_cliente_por_id(id_cliente):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clientes WHERE id_cliente = %s', (id_cliente,))
    dato_cliente = cur.fetchone()
    print("dato_cliente")
    if dato_cliente:
        dato = {'id_cliente': dato_cliente[0], 'nombre': dato_cliente[1], 'apellidos': dato_cliente[2], 'edad': dato_cliente[3], 'telefono': dato_cliente[4],'direccion': dato_cliente[5], 'email': dato_cliente[6]}
        conn.close()
        return jsonify(dato)
    else:
        return 'The client was not found'
    
# Delete a cliente

def del_cliente(id_cliente):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('DELETE FROM clientes WHERE id_cliente = %s', (id_cliente,))
    conn.commit()
    conn.close()
    print("The client was deleted !!")
    return ""