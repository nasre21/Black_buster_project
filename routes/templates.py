from flask import redirect, request, render_template
from database.db import connectdb

def create_user():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cargo = request.form['cargo']
    username = request.form['username']
    password = request.form['password']

    con = connectdb()
    cur = con.cursor()
 
    cur.execute("INSERT INTO empleados (nombre, apellido, cargo) VALUES (%s, %s, %s)", (nombre, apellido, cargo))
    id_empleado = cur.lastrowid
    cur.execute("INSERT INTO users (username, password, id_empleado) VALUES (%s, %s, %s)", (username, password, id_empleado))
    con.commit()
    cur.close()
    con.close()

    return redirect('/movies')

    