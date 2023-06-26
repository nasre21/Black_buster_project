from flask import Flask
from routes.empleados import *
from routes.cliente import *



from routes.films import *
from routes.invetario import *

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


if __name__ == '__main__':
    app.run(debug=True)
