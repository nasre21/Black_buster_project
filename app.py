from flask import Flask
from routes.empleados import *
from routes.cliente import *
from routes.films import *

app = Flask(__name__)

# Roots employs
app.route('/empleado_add', methods=['POST'])(add_empleado)
app.route('/empleados', methods=['GET'])(get_empleados)
app.route('/empleado/<int:id_empleado>')(obtener_empleado_por_id)
app.route('/empleados_del/<int:id_empleado>', methods=['DELETE'])(del_empleado)
app.route("/empleado/<int:id_empleado>", methods=["PATCH"])(update_empleado)

# Roots clients
app.route('/cliente_add', methods=['POST'])(add_cliente)
app.route('/clientes', methods=['GET'])(get_clientes)
app.route('/clientes/<int:id_cliente>', methods=['GET'])(obtener_cliente_por_id)

#Movies Path

app.route('/movies_add', methods =['POST'])(add_movie)
app.route('/movies', methods =['GET'])(get_movie)
app.route('/movies/<int:id_pelicula>', methods=['GET'])(get_one)






if __name__ == '__main__':
    app.run(debug=True)
