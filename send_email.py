from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pymysql as mysql
from plyer import notification
import datetime



def recebe_hora():
    print('Entrou')

    global id_alerta
    global id_tipo_alerta
    global data
    global id_dono
    id_alerta = 0

    mydb = mysql.connect(host='localhost', user='root', password='', db='mydb', charset='utf8mb4')

    cursor = mydb.cursor()

    cursor.execute("select id_alerta, data_alerta, id_dono, id_tipo_alerta from alerta WHERE id_dono = 2 and DATE_SUB(data_alerta, INTERVAL 24 HOUR) <= NOW() and situacao = 1 ")

    resultado = cursor.fetchall()

    while resultado:
        for linha in resultado:
            id_alerta = linha[0]
            data = linha[1]
            id_dono = linha[2]
            id_tipo_alerta = linha[3]
            #data_alerta = data.strftime("%d-%m-%Y")
            #horario_alerta = data.strftime("%H:%M:%S")

            print('saiu')
            return True

    mydb.close()
def recebe_categoria():

    mydb = mysql.connect(host='localhost', user='root', password='', db='mydb', charset='utf8mb4')

    cursor = mydb.cursor()

    cursor.execute("select categoria_alerta from tipo_alerta WHERE id_tipo_alerta = "+str(id_tipo_alerta))

    resultado = cursor.fetchall()

    for linha in resultado:

        categoria_alerta = linha[0]

    if categoria_alerta == "Vacina":

        titulo_email = "Alerta de Vacina! - AssistentePessoalPet"
        texto_email = "Está marcado para amanhã uma vacina do seu melhor amigo! Já se planeja para leva-lo."

    elif categoria_alerta == "Banho":

        titulo_email = "Alerta de Banho! - AssistentePessoalPet"
        texto_email = "Está marcado para amanhã um Banho do seu melhor amigo! Já se planeja para leva-lo."

    elif categoria_alerta == "Outros":

        titulo_email = "Alerta! - AssistentePessoalPet"
        texto_email = "Algo está marcado para amanhã do seu melhor amigo! Já se planeja para leva-lo."

    elif categoria_alerta == "Ração":

        titulo_email = "Alerta de Ração! - AssistentePessoalPet"
        texto_email = "Não deixe seu melhor amigo com fome! A ração dele está acabando."

    mydb.close()

    retorno = {'titulo': titulo_email, 'texto':texto_email}

    return retorno

def send_email(texto):

    # create message object instance
    msg = MIMEMultipart()

    message = texto['texto']
    msg['Subject'] = texto['titulo']

    # setup the parameters of the message
    password = "assistente123"
    msg['From'] = "assistentepet.testes@gmail.com"
    msg['To'] = email_alerta


    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("Successfully sent email to %s" % (msg['To']))

def notifier(texto):

    titulo_notify = texto['titulo']
    texto_notify = texto['texto']

    notification.notify(
        title=titulo_notify,
        message=texto_notify,
        app_name='AssistentePessoalPet',
        app_icon='icone_pet.ico'
    )

def execute_email(email):

    texto = recebe_categoria()

    send_email(texto)
    notifier(texto)

def update_alerta():

    mydb = mysql.connect(host='localhost', user='root', password='', db='mydb', charset='utf8mb4')
    cursor = mydb.cursor(mysql.cursors.DictCursor)
    cursor.execute("UPDATE alerta SET situacao = 0 WHERE id_alerta = %s",(id_alerta))
    cursor.execute("commit");
    mydb.close()

#Chamar essa função para mandar o email, passando o email de destino
def execute_alerta(email_dono):

    global email_alerta

    email_alerta = email_dono

    while True:
        recebe_hora()
        print(id_alerta)
        if id_alerta == 0:

            return True

        else:

            email = email_dono
            execute_email(email)
            update_alerta()
            return True