from flask import Flask
from routes.empleados import *
from routes.cliente import *

app = Flask(__name__)

# Roots employs
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

if __name__ == '__main__':
    app.run(debug=True)
