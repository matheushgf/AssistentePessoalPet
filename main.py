#IMPORTAÇÃO DAS BIBILOTECAS NECESSARIAS
from tkinter import*
import random
import time
import datetime
import recognizer
import registro_pet

#INICIALIZANDO O OBJETO GRAFICO DA TELA
root = Tk()

#PASSANDO AS MEDIDAS E CONFIGURAÇÃO DA TELA
root.geometry("640x480+0+0")
root.title("PetSystem")
root.configure(background='#707070')

#CRIANDO O FRAME DO TOPO
Top = Frame(root, width=640, height= 50, bd=4)
Top.pack(side=TOP)
Top.configure(background='black')

Top2 = Frame(root, width=640, height= 400)
Top2.pack(side=TOP)
Top2.configure(background='#707070')

#CRIANDO O FRAME INFERIOR 
Bottom = Frame(root, width=640, height= 442, bd=4)
Bottom.pack(side=BOTTOM)
Bottom.configure(background='light blue')

#INSERINDO LABEL PARA TITULO DO SISTEMA
lblTitulo = Label(Top,font=('arial', 15, 'bold'), text="PETSystem", width='52')
lblTitulo.grid(row=0, column=0)
label2=StringVar()
label2.set("Diga o comando que você quer executar\n após ativar o botão de reconhecimento:")
lblRecognizerText= Label(Top2,font=('arial', 12), textvariable=label2, bd=4, relief='solid',bg='light blue')
lblRecognizerText.grid(row=0, column=0,columnspan=1,pady=170)

def button_click():
    resultado = recognizer.recognizer()
    mensagem = recognizer.command_verification(resultado)

    label2.set(mensagem)

#BOTÕES INFERIORES
reconActivate = Button(Bottom,padx=15, pady=1, bd=1, fg='black', font=('arial',12), width=20,
                       text="ATIVAR RECONHECIMENTO",command=button_click).grid(row=0, column=0)


#FINALIZAÇÃO DA TELA DE SISTEMA
root.mainloop()
