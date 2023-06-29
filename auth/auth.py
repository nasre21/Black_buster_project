from flask import redirect, render_template, request, url_for, session, flash
from database.db import connectdb
import jwt
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username_db' not in session:
            # El usuario no ha iniciado sesión, redirigir al inicio de sesión
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        con = connectdb()
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s ", (username,))
        result = cur.fetchone()

        if result is not None:
            username_db = result[1]
            password_db = result[2]

            password_uncoded = jwt.decode(password_db, options={"verify_signature": False})

            if username == username_db and password == password_uncoded["password"]:
                session["username_db"] = username_db
                return redirect("/movies")

        error_message = "El usuario o la contraseña son incorrectos."
        return render_template("login.html", error_message=error_message)

    return render_template("login.html")



def logout():
    session.pop('username_db', None)
    session['logged_in'] = False
    
    flash('Sesión cerrada correctamente')
    return redirect(url_for('login'))

