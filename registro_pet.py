from tkinter import *
import tkinter.messagebox as MessageBox
import pymysql as mysql
import recognizer

# ---------------------------- FUNÇÕES DO CADASTRO ---------------------------- #
# Captura dos dados recebidos pelos usuário, Nome e tipo do animal e adiciona ao banco.
def insert():
    if str(txtnome)=="" or str(txttipo)=="":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        mydb = mysql.connect(host='localhost', user='petuser', password='', db='bancopet', charset='utf8mb4')
        cursor = mydb.cursor(mysql.cursors.DictCursor)
        cursor.execute("INSERT INTO bancopet.pet (nome_pet, tipo_pet, id_donopet) "
                       "VALUES ('"+ txtnome.get().title() +"','"+ txttipo.get().title() +"',1)")
        cursor.execute("commit");
        MessageBox.showinfo("Status da ação", "Dados inseridos com sucesso");
        mydb.close()

# Reconhece informação por voz para o nome do pet.
def nomepet():
    txtnomelocal = recognizer.recognizer()
    txtnome.set(txtnomelocal.title())

# Reconhece informação por voz para o tipo do pet.
def tipopet():
    txttipolocal = recognizer.recognizer()
    txttipo.set(txttipolocal.title())

# Apaga valores das labels
def clear():
    txtnome.set("Nome do pet")
    txttipo.set("Tipo do pet")

# ------------------------------ TKINTER INTERFACE ------------------------------ #
def registro_pet():

    janela = Tk()
    janela.geometry("350x500+500+200")
    janela.wm_title("Assistente Pet")
    lbltitulo = Label(janela, text="REGISTRO DO PET", font=("Arial", 10, "bold")).place(x=110, y=10)

    # ===== VARIAVEIS LOCAIS ===== #
    txtnome = StringVar()
    txttipo = StringVar()
    txtnome.set("Nome do pet")
    txttipo.set("Tipo do pet")

    # Labels de idenficação dos campos
    lblnome = Label(janela, text="Nome do Pet:", font=("Arial", 8, "bold")).place(x=10, y=70)
    lbltipo = Label(janela, text="Tipo do Pet:", font=("Arial", 8, "bold")).place(x=10, y=150)

    # Labels que aparecerão as respostas para nome e tipo do pet
    entnome = Label(janela, font=("Arial", 10), bg='white', width='30', height='2', textvariable=txtnome)
    entnome.place(x=90, y=90)
    enttipo = Label(janela, font=("Arial", 10), bg='white', width='30', height='2', textvariable=txttipo)
    enttipo.place(x=90, y=170)

    # Botões para ouvir o usuário
    petbt = Button(janela, text='Diga NOME \ndo pet:', command=nomepet)
    petbt.place(x=10, y=90)
    tipobt = Button(janela, text='Diga o TIPO \ndo pet:', command=tipopet)
    tipobt.place(x=10, y=170)

    #Botões de ação, confirmar o cadastro ou apagar.
    btok = Button(janela, width=10, text="Confirmar", bg="light green", command=insert).place(x=30, y=300)
    btdel = Button(janela, width=10, text="Apagar", bg="red", command=clear).place(x=230, y=300)

    janela.mainloop()