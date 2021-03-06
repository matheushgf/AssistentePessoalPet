#IMPORTAÇÃO DAS BIBILOTECAS NECESSARIAS

from tkinter import*
import random
import time
import datetime
import recognizer
import send_email
import threading
import pyttsx3

def speech():
    label2audio = ('Diga o comando que você quer executar após clicar no microfone')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def notifier():
    email = "eduardo.alexandre.ferreira@gmail.com"
    print("Deu certo! Está mandando email para:")
    print(email)
    while True:
        time.sleep(60)
        send_email.execute_alerta(email)

t = threading.Thread(name='my_notifier', target=notifier)
t.start()

#INICIALIZANDO O OBJETO GRAFICO DA TELA
root = Tk()
btnimage=PhotoImage(file="microfone.png")

#PASSANDO AS MEDIDAS E CONFIGURAÇÃO DA TELA
root.geometry("400x320+0+0")
root.title("AssistentePet")
root.configure(background='#707070')

#CRIANDO OS FRAMES DO TOPO
Top = Frame(root, width=400, height= 25, bd=0)
Top.pack(side=TOP)
Top.configure(background='black')

Top2 = Frame(root, width=400, height=75)
Top2.pack(side=TOP)
Top2.configure(background='#707070')

Top3 = Frame(root, width=400, height=25)
Top3.pack(side=TOP)
Top3.configure(background='blue')

#CRIANDO OS FRAMES INFERIORES
Bottom = Frame(root, width=400, height= 25, bd=1)
Bottom.pack(side=BOTTOM)
Bottom.configure(background='black')

Bottom2 = Frame(root, width=400, height= 12.5, bd=1)
Bottom2.pack(side=BOTTOM)
Bottom2.configure(background='#707070')

#FRAME DE EXIBIÇÃO DE INSTRUÇÕES
Bottom3 = Frame(root, width=400, height= 12.5, bd=1)
Bottom3.pack(side=BOTTOM)
Bottom3.configure(background='light blue')

#INSERINDO LABEL PARA TITULO DO SISTEMA
lblTitulo = Label(Top,font=('arial', 15), text="AssistentePET", width='36')
lblTitulo.grid(row=0, column=0)

#INSERINDO LABEL PARA LINHA DE EXIBIÇÃO DE INSTRUÇÕES EXECUTADAS
label2=StringVar()
label2.set("Diga o comando que você quer executar\n após clicar no microfone:")
lblRecognizerText= Label(Bottom3,font=('arial', 12), textvariable=label2, bd=1, relief='solid',bg='light blue')
lblRecognizerText.grid(row=0, column=0,columnspan=1,pady=0)

#INSERINDO LABEL DO RODAPÉ
lblRodapeText = Label(Bottom,font=('arial', 8), text="Desenvolvido pelo Grupo 06 - BD Fatec SJC", width='66',bg='light blue')
lblRodapeText.grid(row=0, column=0)

#FUNÇÃO PARA VALIDAÇÃO DE COMANDOS
def button_click():
    while True:
        try:
            resultado = recognizer.recognizer()
            mensagem = recognizer.command_verification(resultado)
            label2.set(mensagem)
            break
        except:
            print("Voz não detectada. Repita novamente.")
            label2.set("Voz não detectada. Repita novamente.")
            button_click()

#BOTÕES INFERIORES

reconActivate = Button(Top3,padx=1, pady=110, bd=1, fg='black', font=('arial',12),
text="ATIVAR RECONHECIMENTO",command=button_click,image=btnimage).grid(row=0, column=0)


t = threading.Thread(target=speech)
t.start()
#FINALIZAÇÃO DA TELA DE SISTEMA

root.mainloop()
#program_not.execute_alerta()
