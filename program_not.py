import time
from typing import Any, Union

from pymysql.cursors import Cursor
import send_email
import pymysql as mysql

global id_tipo_alerta
global id_alerta

def recebe_hora():

    mydb = mysql.connect(host='localhost', user='root', password='', db='mydb', charset='utf8mb4')

    cursor = mydb.cursor()

    resultado = cursor.execute("select id_alerta, data_alerta, id_dono, id_tipo_alerta from alerta WHERE id_dono = 2 and DATE_SUB(data_alerta, INTERVAL 24 HOUR) <= NOW() and situacao = 1 ")

    resultado = cursor.fetchall()

    for linha in resultado:
        id_alerta = linha[0]
        data = linha[1]
        id_dono = linha[2]
        id_tipo_alerta = linha[3]

        data_alerta = data.strftime("%d-%m-%Y")
        horario_alerta = data.strftime("%H:%M:%S")
    
    mydb.close()

    return True


def execute_alerta():

    while True:

        if recebe_hora():

            email = 'cesar.ruan84@gmail.com'
            send_email.execute_email(email, id_alerta, id_tipo_alerta)
            #update_situacao(sql_recebe['id_alerta'])


while True:
    
    time.sleep(60)
    execute_alerta()
    
