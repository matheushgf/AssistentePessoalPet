'''
Registro peso
'''
from tkinter import *
#from get_tables_field import *
#from insert import *


registro_peso = []  #Salvar no banco.
registro_racao = []  #Salvar no banco.
'''
def reg():
    str(reg_pes.get())
    registro_peso.append(reg_pes.get())

    str(reg_rac)
    registro_racao.append(reg_rac.get())
'''
def validad():

    if not reg_pes.get().isnumeric() and len(reg_pes.get()) == 0 and str(reg_pes.get()) == '':

        txt_peso["text"] = 'Dado inválido, digite novamente.'

    else:

        str(reg_pes.get())
        registro_peso.append(reg_pes.get())

    if not reg_rac.get().isnumeric() and len(reg_rac.get()) == 0 and str(reg_rac.get()) == '':

        pass

    else:

        str(reg_rac)
        registro_racao.append(reg_rac.get())


janela = Tk()

#Campos de registro
reg_pes = Entry(janela, width=50)
reg_pes.place(x=40, y=130)

reg_rac = Entry(janela, width=50)
reg_rac.place(x=40, y=220)

#Texto de cada campo
tex_pes = Label(janela, text="Peso:")
tex_pes.place(x=40, y=110)

tex_reg = Label(janela, text="Qtde Ração:")
tex_reg.place(x=40, y=200)

#Mensagem de erro para o usuário.
lb_peso = Label(janela, text='')
lb_peso.place(x=225, y=155)

lb_racao = Label(janela, text='')
lb_racao.place(x=225, y=245)

legenda = Label(janela, texto= 'Nos informe o peso e a ração do Pet')
legenda.place(x=200, y=50)

#Botão de salvamento
bt = Button(janela, width=20, text="OK", command=validad)
bt.place(x=150, y=400)



janela.title("Registro")
janela.geometry("500x500+300+300")
janela.mainloop()

print(registro_peso, registro_racao)