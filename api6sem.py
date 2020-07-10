import pyttsx3
import threading
import requests
import json
from tkinter import *

def dicasDeFilme():

    r = requests.get('http://topicos-avancados.herokuapp.com/getFilme/6')

    if (r.status_code != 200):
        print('Não foi possível obter o filme pela API.')
    else:
        try:
            filmeGet = json.loads(r.text)
            textoFalado = f"A dica de filme de hoje para assistir agora \n com seu pet de estimação é: \n {filmeGet['filme']}"
        except:
            print("Erro na conversão de json para string")

    root = Tk()

    def speech():
        label2audio = (textoFalado)
        en = pyttsx3.init()
        en.say(label2audio)
        en.runAndWait()


    # PASSANDO AS MEDIDAS E CONFIGURAÇÃO DA TELA
    root.geometry("400x320+0+0")
    root.title("Dica de Filme")
    root.configure(background='#707070')

    # CONFIGURANDO O TEMPORIZADOR DE FECHAMENTO DA TELA
    root.after(10000, lambda: root.destroy())

    lblTitulo = Label(root, font=('arial', 9), text=textoFalado, width='55').place(x=5, y=90, height=50)

    t = threading.Thread(target=speech)
    t.start()
    root.mainloop()