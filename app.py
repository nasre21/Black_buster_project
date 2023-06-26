from flask import Flask
from routes.empleados import *
from routes.cliente import *
from routes.pagos import *
from routes.alquiler import *
from routes.inventario import *

app = Flask(__name__)

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


# Routes Alquiler
app.route('/alquiler/info/<titulo>', methods=['GET'])(obtener_info_por_titulo)


# Routes inventario
app.route('/inventario', methods=['GET'])(get_inventario)

if __name__ == '__main__':
    app.run(debug=True)
