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

# Update a client

def update_cliente(id_cliente):
    conn = connectdb()
    cur = conn.cursor()

    data = request.get_json()

    if "nombre" in data:
        nombre = data["nombre"]
        cur.execute('UPDATE clientes SET nombre = %s WHERE id_cliente = %s', (nombre, id_cliente))

    if "apellidos" in data:
        apellidos = data["apellidos"]
        cur.execute('UPDATE clientes SET apellidos = %s WHERE id_cliente = %s', (apellidos, id_cliente))

    if "edad" in data:
        edad = data["edad"]
        cur.execute('UPDATE clientes SET edad = %s WHERE id_cliente = %s', (edad, id_cliente))

    if "telefono" in data:
        telefono = data["telefono"]
        cur.execute('UPDATE clientes SET telefono = %s WHERE id_cliente = %s', (telefono, id_cliente))

    if "direccion" in data:
        direccion = data["direccion"]
        cur.execute('UPDATE clientes SET direccion = %s WHERE id_cliente = %s', (direccion, id_cliente)) 

    if "email" in data:
        email = data["email"]
        cur.execute('UPDATE clientes SET email = %s WHERE id_cliente = %s', (email, id_cliente))       
    conn.commit()
    conn.close()

    return 'Dates modified'

# Get client by phone number

def obtener_cliente_por_telefono(cliente_telefono):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clientes WHERE telefono = %s', (cliente_telefono,))
    clientes = cur.fetchall()
    print("clientes")
    if clientes:
        data = [{'id_cliente': dato[0], 'nombre': dato[1], 'apellidos': dato[2], 'edad': dato[3], 'telefono': dato[4],'direccion': dato[5], 'email': dato[6]} for dato in clientes]
        conn.close()
        return jsonify(data)
    else:
        return 'No client was found with this phone number'
    
# Get client by email address

def get_client_by_email(cliente_email):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clientes WHERE email = %s', (cliente_email,))
    clientes = cur.fetchall()
    print("clientes")
    if clientes:
        data = [{'id_cliente': dato[0], 'nombre': dato[1], 'apellidos': dato[2], 'edad': dato[3], 'telefono': dato[4],'direccion': dato[5], 'email': dato[6]} for dato in clientes]
        conn.close()
        return jsonify(data)
    else:
        return 'No client was found with this email address'


# Get client by email address

def get_clients_over_18(cliente_edad):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clientes WHERE edad >= %s', (cliente_edad,))
    clientes = cur.fetchall()
    print("clientes")
    if cliente_edad >= 18:
        data = [{'id_cliente': dato[0], 'nombre': dato[1], 'apellidos': dato[2], 'edad': dato[3], 'telefono': dato[4],'direccion': dato[5], 'email': dato[6]} for dato in clientes]
        conn.close()
        return jsonify(data)
    else:
        return 'No results were found'
    
    # Obtain a client by id

def check_age(id_cliente):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clientes WHERE id_cliente = %s', (id_cliente,))
    dato_cliente = cur.fetchone()
    print("dato_cliente")
    if dato_cliente[3] >= 18:
        # dato = {"""'id_cliente': dato_cliente[0], 'nombre': dato_cliente[1],
        #         'apellidos': dato_cliente[2], 'edad': dato_cliente[3],
        #         'telefono': dato_cliente[4],'direccion': dato_cliente[5], 'email': dato_cliente[6]"""}
        conn.close()
        return 'You can rent this movie'
    else:
        return 'You are underage to rent this movie'