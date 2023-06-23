from flask import Flask
from routes.empleados import *
from routes.cliente import *
from routes.pagos import *

app = Flask(__name__)

# Rutas empleados
app.route('/empleado_add', methods=['POST'])(add_empleado)
app.route('/empleados', methods=['GET'])(get_empleados)
app.route('/empleado/<int:id_empleado>')(obtener_empleado_por_id)
app.route('/empleados_del/<int:id_empleado>', methods=['DELETE'])(del_empleado)
app.route("/empleado/<int:id_empleado>", methods=["PATCH"])(update_empleado)


#PAGOS
app.route("/pagos", methods=["GET"])(get_payments)

app.route("/pago/<int:id_pago>", methods=["GET"])(get_payment_by_id)

app.route("/pago", methods=["POST"])(add_pagos) 

app.route("/pagos_del/<int:id_pago>", methods=["DELETE"])(del_payment)

app.route("/pagos_desc", methods=["GET"])(get_payment_desc)

app.route("/pagos_asc", methods=["GET"])(get_payment_asc)
# Roots cliente nueva
app.route('/cliente_add', methods=['POST'])(add_cliente)

if __name__ == '__main__':
    app.run(debug=True)
