#IMPORTAÇÃO DAS BIBILOTECAS NECESSARIAS
from tkinter import*
import tkinter
import random
import time
import datetime
import recognizer

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
    resultado = recognizer.recognizer()
    flag=recognizer.command_verification(resultado)
    if flag == True:
        label2.set("Comando Reconhecido. Encaminhando função...")
    else:
        label2.set("Comando invalido. Tente novamente")

#BOTÕES INFERIORES

reconActivate = Button(Top3,padx=1, pady=110, bd=1, fg='black', font=('arial',12),
text="ATIVAR RECONHECIMENTO",command=button_click,image=btnimage).grid(row=0, column=0)

#FINALIZAÇÃO DA TELA DE SISTEMA
root.mainloop()
