from flask import jsonify, redirect, request, session
from database.db import connectdb
from auth.auth import *



def     create_user(nombre, apellido, cargo, username, password):

    username = request.form.get('username')
    password = request.form.get('password')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    cargo = request.form.get('cargo')

    payload = {"password": password}
    token = generate_token(payload)

    try:
        with connectdb() as con:
            cur = con.cursor()

            cur.execute("START TRANSACTION")

            cur.execute(
                "INSERT INTO empleados (nombre, apellido, cargo) VALUES (%s, %s, %s)",
                (nombre, apellido, cargo)
            )
            id_empleado = cur.lastrowid

            cur.execute(
                "INSERT INTO users (id_empleado, username, password) VALUES (%s, %s, %s)",
                (id_empleado, username, token)
            )

            con.commit()

            return jsonify({'message': 'User created successfully'})

    except Exception as e:
        con.rollback()
        return jsonify({'error': str(e)})

    finally:
        cur.close()



def login(username, password):
    con = connectdb()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result is not None:
        username_db = result[1]
        password_db = result[2]
        password_uncoded = decode_token(password_db)

        if username_db == username and password_uncoded == password:
            session['username'] = username
            session['password'] = password
            return redirect('/panel')

    return False



    