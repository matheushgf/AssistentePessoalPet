'''
Registro peso
'''
from tkinter import *
#from get_tables_field import *
#from insert import *



reg_racao = []  #Implementar no banco.
def reg_bd():

    str(reg.get())
    reg_racao.append(reg.get())


janela = Tk()

reg = Entry(janela, width=15)
reg.place(x=120, y=100)

bt = Button(janela, width=20, text="OK", command=reg_bd)
bt.place(x=60, y=130)

lb = Label(janela, text="Registro de Ração")
lb.place(x=75, y=75)

tex_reg = Label(janela, text="Quantidade: Kg")
tex_reg.place(x=10, y=100)

#if :

    #msg = Label(janela, text="Registro salvo com Sucesso.")
    #msg.place(x=50, y=175)

janela.title("APP")
janela.geometry("300x300+300+300")
janela.mainloop()

print(reg_racao)  #Apenas para demonstração de execução.