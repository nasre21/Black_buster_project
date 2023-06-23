import datetime
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
    
#add payments
def add_pagos():
    con = connectdb()
    cur = con.cursor()
    data = request.get_json()

    monto = data['monto']
    fecha_pago = datetime.date.today().strftime('%Y-%m-%d')
    metodo = data['metodo']

    cur.execute('insert into pago(monto,fecha_pago,metodo) values(%s,%s,%s)', (monto,fecha_pago,metodo))
    con.commit()
    con.close()
    print('pago creado')
    return"Pago agregar"


#delete payment

def del_payment(id_pago):
    con = connectdb()
    cur = con.cursor()
    cur.execute('DELETE FROM pago WHERE id_pago = %s', (id_pago,))
    con.commit()
    con.close()
    print("pago eliminado !!")
    return {"message":"pago eliminado"}

#get payment by desc

def get_payment_desc():
    con = connectdb()
    cur = con.cursor()
    cur.execute('SELECT * FROM pago order by monto desc')
    datos_pago = cur.fetchall()
    data = [{'id_pago':pago[0], 'monto':pago[1],'fecha_pago':pago[2], 'metodo':pago[3]}for pago in datos_pago]
    con.close()
    return data

def get_payment_asc():
    con = connectdb()
    cur = con.cursor()
    cur.execute('SELECT * FROM pago order by monto asc')
    datos_pago = cur.fetchall()
    data = [{'id_pago':pago[0], 'monto':pago[1],'fecha_pago':pago[2], 'metodo':pago[3]}for pago in datos_pago]
    con.close()
    return data