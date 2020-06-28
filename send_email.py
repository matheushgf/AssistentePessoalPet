from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pymysql as mysql
from plyer import notification

def recebe_categoria():
    mydb = mysql.connect(host='localhost', user='root', password='', db='mydb', charset='utf8mb4')

    cursor = mydb.cursor()

    resultado = cursor.execute("select categoria_alerta from tipo_alerta WHERE id_tipo_alerta = "+str(id_tipo_alert))

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
        app_icon='pet_store_shop_building_animal_icon_124625.ico'
    )

def execute_email(email, id_alerta, id_tipo_alerta):

    global email_alerta
    global id_alert
    global id_tipo_alert
    global titulo_email
    global texto_email
    global categoria

    email_alerta = email
    id_alert = id_alerta
    id_tipo_alert = int(id_tipo_alerta)

    texto = recebe_categoria()
    #print(titulo_email)
    #print(texto_email)

    send_email(texto)
    notifier(texto)