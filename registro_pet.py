from tkinter import *
import tkinter.messagebox as MessageBox
import pymysql as mysql

# ---------------------------- FUNÇÕES DE CADASTRO ---------------------------- #
def insert():
    txtnome = entnome.get()
    txttipo = enttipo.get();

    if(str(txtnome)=="" or str(txttipo)==""):
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        mydb = mysql.connect(host='localhost', user='petuser', password='', db='bancopet', charset='utf8mb4')
        cursor = mydb.cursor(mysql.cursors.DictCursor)
        cursor.execute("INSERT INTO bancopet.pet (nome_pet, tipo_pet, id_donopet) VALUES ('"+ txtnome +"','"+ txttipo
                       +"',1)")
        cursor.execute("commit");
        MessageBox.showinfo("Status da ação", "Dados inseridos com sucesso");
        con.close()

def clear():
    entnome.delete(0, END)
    enttipo.delete(0, END)

# ------------------------------ TKINTER INTERFACE ------------------------------ #
janela = Tk()
janela.geometry("350x500+500+200")
janela.wm_title("Assistente Pet")
lbltitulo = Label(janela, text="REGISTRO DO PET", font=("Arial", 10, "bold")).place(x=110, y=10)

# Campos de entradas
lblnome = Label(janela, text="Nome do Pet:", font=("Arial", 8, "bold")).place(x=10, y=70)
lbltipo = Label(janela, text="Tipo do Pet:", font=("Arial", 8, "bold")).place(x=10, y=150)

entnome = Entry(janela, font=("Arial", 10), width=45)
entnome.place(x=10, y=90)
enttipo = Entry(janela, font=("Arial", 10), width=45)
enttipo.place(x=10, y=170)


#Botões de ação, confirmar o cadastro ou apagar.
btok = Button(janela, width=10, text="Confirmar", bg="light green", command=insert).place(x=30, y=300)
btdel = Button(janela, width=10, text="Apagar", bg="red", command=clear).place(x=230, y=300)

janela.mainloop()
