from flask import jsonify, request
from database.db import connectdb

def create_user(username, password):
    try:
        con = connectdb()
        cur = con.cursor()

        cur.execute("START TRANSACTION")

        cur.execute("""
            INSERT INTO empleados (nombre, apellido, cargo)
            VALUES (%s, %s, %s)
        """, ('Anyell', 'Mendoza Lopez', 'Dependiente'))

        id_empleado = cur.lastrowid

        cur.execute("""
            INSERT INTO users (id_empleado, username, password)
            VALUES (%s, %s, %s)
        """, (id_empleado, username, password))

        con.commit()

        return jsonify({'message': 'User created successfully'})

    except Exception as e:
        con.rollback()
        return jsonify({'error': str(e)})

    finally:
        cur.close()
        con.close()
