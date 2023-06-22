from flask import jsonify, request
from database.db import connectdb

def get_payments():
    con =  connectdb()
    cur = con.cursor()

    cur.execute("SELECT * FROM pago;")
    pagos = cur.fetchall()
    datos_pago = [{'id_pago':pago[0], 'monto':pago[1],'fecha_pago':pago[2], 'metodo':pago[3]}for pago in pagos]
    con.close()

    return jsonify(datos_pago)


#get payment by id
def get_payment_by_id(id_pago):
    con = connectdb()
    cur = con.cursor()

    cur.execute("SELECT * FROM pago WHERE id_pago = %s", (id_pago,))
    pagos = cur.fetchone()

    if pagos:
        dato ={'id_pago':pagos[0],'monto':pagos[1],'fecha_pago':pagos[2],'metodo':pagos[3]}
        con.close()
        return jsonify(dato)
    else:
        return 'pagos no encontradas'
    
