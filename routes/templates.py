from flask import jsonify, redirect, render_template, request, session
from database.db import connectdb
from auth.auth import *
from app import app

app.secret_key = 'secret'



def     create_user(nombre, apellido, cargo, username, password):
    con = connectdb()
    cur = con.cursor()
   
    username = request.form.get('username')
    password = request.form.get('password')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    cargo = request.form.get('cargo')

    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
            error_message = (
                "El usuario ya existe. Por favor, elige otro nombre de usuario."
            )
            return render_template("registro.html", error_message=error_message)



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




    