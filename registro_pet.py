from tkinter import *
import tkinter.messagebox as MessageBox
from petassistant import recognizer
from petassistant import crud

# ---------------------------- FUNÇÕES DO CADASTRO ---------------------------- #
# Captura dos dados recebidos pelos usuário, Nome e tipo do animal e adiciona ao banco.
def insert():
    if str(entnome['text'])=="" or str(enttipo['text'])=="":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        nome = entnome['text']
        if enttipo['text'] == "Cachorro":
            id_tipo = 1
        elif enttipo['text'] == "Gato":
            id_tipo = 2
        else:
            id_tipo = 3
        nome_tabela = 'pet'
        dados = {'nome_pet': nome, 'id_tipo_pet': id_tipo}
        crud.insert(nome_tabela, dados)

# Reconhece informação por voz para o nome do pet.
def nomepet():
    txtnomelocal = recognizer.recognizer()
    entnome['text'] = (txtnomelocal.title())


# Reconhece informação por voz para o tipo do pet.
def tipopet():
    txttipolocal = recognizer.recognizer()
    enttipo['text'] = (txttipolocal.title())


# Apaga valores das labels
def clear():
    entnome['text'] = ''
    enttipo['text'] = ''
    #txtnome.set("Nome do pet")

# ------------------------------ TKINTER INTERFACE ------------------------------ #

def registro_pet():
    janela = Tk()
    janela.geometry("350x500+500+200")
    janela.wm_title("Assistente Pet")
    lbltitulo = Label(janela, text="REGISTRO DO PET", font=("Arial", 10, "bold")).place(x=110, y=10)

    # ===== VARIAVEIS LOCAIS ===== #
    global entnome
    global enttipo
    entnome = StringVar()
    enttipo = StringVar()
#    txtnome.set("Nome do pet")
#    txttipo.set("Tipo do pet")

    # Labels de idenficação dos campos
    lblnome = Label(janela, text="Nome do Pet:", font=("Arial", 8, "bold")).place(x=10, y=70)
    lbltipo = Label(janela, text="Tipo do Pet:", font=("Arial", 8, "bold")).place(x=10, y=150)

    # Labels que aparecerão as respostas para nome e tipo do pet
    '''
    entnome = Label(janela, font=("Arial", 10), bg='white', width='30', height='2', textvariable=txtnome)
    entnome.place(x=90, y=90)
    enttipo = Label(janela, font=("Arial", 10), bg='white', width='30', height='2', textvariable=txttipo)
    enttipo.place(x=90, y=170)
    '''
    entnome = Label(janela, font=("Arial", 10), bg='white', width='30', height='2', text='Qual o nome do seu pet?')
    entnome.place(x=90, y=90)
    enttipo = Label(janela, font=("Arial", 10), bg='white', width='30', height='2', text='Que tipo é o pet?')
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

#registro_pet()