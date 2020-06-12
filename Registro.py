'''
Registro peso
'''
from tkinter import *
#from get_tables_field import *
#from insert import *

registro_peso = []  #Salvar no banco.
registro_racao = []  #
reg_rac_min = 0

def validad():

    #Fazer laço para caso os dados sejam letras

    global reg_rac_min
    reg_rac_min = float(reg_pes.get()) * 0.03

    if not reg_pes.get().isnumeric() and len(reg_pes.get()) == 0 and str(reg_pes.get()) == '':

        lb_peso["text"] = 'Dado inválido, digite novamente.'

    else:

        if not reg_rac.get().isnumeric() and len(reg_rac.get()) == 0 and str(reg_rac.get()) == '':

            lb_racao["text"] = 'Dado inválido, digite novamente.'

        elif float(reg_rac.get()) <= reg_rac_min:  # Condição de invalidez por minimo.

            rac["text"] = 'A quantidade de ração não pode ser menos que o mínimo indicado!'

        else:

            lb_peso["text"] = ''
            lb_racao["text"] = ''
            save["text"] = 'Dados salvos com sucesso.'

            str(reg_rac)
            registro_racao.append(reg_rac.get())

            str(reg_pes.get())
            registro_peso.append(reg_pes.get())

#Interface gráfica
janela = Tk()

#Campos de registro.
reg_pes = Entry(janela, width=50)
reg_pes.place(x=40, y=130)

reg_rac = Entry(janela, width=50)
reg_rac.place(x=40, y=220)

#Textos de cada campo.
tex_pes = Label(janela, text="Peso:")
tex_pes.place(x=40, y=110)

tex_reg = Label(janela, text="Qtde Ração:")
tex_reg.place(x=40, y=195)

#Mensagens de erro ou informativa para o usuário.
lb_peso = Label(janela, text='')
lb_peso.place(x=225, y=155)

lb_racao = Label(janela, text='')
lb_racao.place(x=225, y=245)

save = Label(janela, text= '')
save.place(x=155, y=360)

rac = Label(janela, text='')
rac.place(x=35, y=280)

#Botão de salvamento
bt = Button(janela, width=20, text="OK", command=validad)
bt.place(x=150, y=400)

janela.title("Registro")
janela.geometry("500x500+300+300")
janela.mainloop()

print(registro_peso, registro_racao)
