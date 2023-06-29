from flask import Flask
import jwt
from auth.auth import *
from routes.empleados import *
from routes.cliente import *
from routes.pagos import *
from routes.alquiler import *
from routes.inventario import *
from routes.films import *
from routes.inventario import *

app = Flask(__name__)
app.secret_key = "otorinolaringolo"

# Rutas empleados
app.route('/empleado_add', methods=['POST'])(add_empleado)
app.route('/empleados', methods=['GET'])(get_empleados)
app.route('/empleado/<int:id_empleado>')(obtener_empleado_por_id)
app.route('/empleados_del/<int:id_empleado>', methods=['DELETE'])(del_empleado)
app.route("/empleado/<int:id_empleado>", methods=["PATCH"])(update_empleado)

# Roots clients
app.route('/clientes', methods=['POST'])(add_cliente)
app.route('/clientes', methods=['GET'])(get_clientes)
app.route('/clientes/<int:id_cliente>', methods=['GET'])(obtener_cliente_por_id)
app.route('/clientes/<int:id_cliente>', methods=['DELETE'])(del_cliente)
app.route("/clientes/<int:id_cliente>", methods=["PATCH"])(update_cliente)
app.route('/clientes/tel/<int:cliente_telefono>', methods=['GET'])(obtener_cliente_por_telefono)
app.route('/clientes/email/<cliente_email>', methods=['GET'])(get_client_by_email)
app.route('/clientes/edad/<int:cliente_edad>', methods=['GET'])(get_clients_over_18)
app.route('/clientes/mayor/<int:id_cliente>', methods=['GET'])(check_age)
#PAGOS
app.route("/pagos", methods=["GET"])(get_payments)

app.route("/pago/<int:id_pago>", methods=["GET"])(get_payment_by_id)

app.route("/pago", methods=["POST"])(add_pagos) 

app.route("/pagos_del/<int:id_pago>", methods=["DELETE"])(del_payment)

app.route("/pagos_desc", methods=["GET"])(get_payment_desc)

app.route("/pagos_asc", methods=["GET"])(get_payment_asc)


# Routes Alquiler""
app.route('/alquiler/all_registers', methods=['GET'])(obtener_info_todas_alquiler)
app.route("/alquiler/info_register_inventary/<titulo>", methods=["GET"])(obtener_info_por_titulo)
app.route("/alquiler/info_register_all", methods=["GET"])(obtener_info_todas_peliculas)
app.route("/alquiler/new_register", methods=["POST"])(add_rent)
app.route("/alquiler/return/<id_alquiler>", methods=['PUT', 'PATCH', 'GET'])(return_movie)






# Routes inventario
app.route('/inventario', methods=['GET'])(get_inventario)

#Movies Path

app.route('/movies_add', methods =['POST'])(add_movie)
app.route('/movies', methods =['GET'])(get_movie)
app.route('/movies/<int:id_pelicula>', methods=['GET'])(get_one)
app.route('/movies_del/<int:id_pelicula>', methods=['DELETE'])(del_movie)
app.route("/movies/<int:id_pelicula>", methods=["PATCH"])(update_pelicula)
app.route('/movies/<int:id_pelicula>', methods=['GET'])(get_one)

# Consulting


app.route('/movies/max', methods=['GET'])(max_peliculas)
app.route('/movies/min', methods=['GET'])(min_peliculas)
app.route('/movies/categoria', methods=['GET'])(categoria_peliculas)
app.route('/movies/director', methods=['GET'])(director_peliculas)
app.route('/movies/año', methods=['GET'])(año_peliculas)


# inventeraio

app.route('/inventario', methods=['GET'])(get_inventario)
app.route('/inventario/<int:id_pelicula>', methods=['GET'])(get_one_inventario)

#login, inicio de sesión y cerrar sesión

app.route("/", methods=["GET","POST"])(login)
app.route('/logout', methods=['POST'])(logout)
app.route("/dashboard")(login_required(dashboard))


  

#######################YORLIN #####################
#Creando mi Decorador para la consulta de la pelicula

app.route("/buscar-titulo", methods=["GET", "POST"])(buscarTitulo)

#Redireccionando cuando la página no existe
# @app.errorhandler(404)
# def not_found(error):
#         return render_template("busqueda.html")

if __name__ == '__main__':
    app.run(debug=True)
