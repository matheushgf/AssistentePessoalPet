from tkinter import *
from tkinter import messagebox, Toplevel
from tkinter.ttk import *
import datetime
import os
import string
import random
import time
from tkinter import *
from PIL import ImageTk, Image


########################################################################################################################

def combine_func(*funcs):
    def combined_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_funcs


########################################################################################################################

def faq_screen():

    faq_screen = Tk()
    faq_screen.configure(background='light blue')
    faq_screen.title("Teste - Projeto Integrador")
    faq_screen.geometry("800x600")
    faq_screen.state("zoomed")
    faq_screen.resizable(False, False)
    faq_screen.attributes("-fullscreen", False)  # Deixa em Fullscreen

    T = Label(faq_screen, anchor="n", bg="light blue", text="Programa ainda em Desenvolvimento e em testes\n"
                                                            "\n"
                                                            "Interface gráfica Desenvolvido por: Renan Moreira Pereira - BD 2020\n"
                                                            "Email: renanrhoads@gmail.com\n"
                                                            "Cel.:(12)98812-6367\n"
                                                            "Ramal:7608")

    T.config(font=("Courier", 12))
    T.place(x=250, y=200)

    Version = Label(faq_screen, anchor="e", bg="light blue", text="Versão: InDev 1.10")
    Version.config(font=("Arial", 12))
    Version.place(x=250, y=550)

    Close = Button(faq_screen, anchor="w", text="Okay", bg="light blue", command=faq_screen.destroy)
    Close.place(x=800, y=570)


########################################################################################################################

def start():
    global start
    global usuario_verify
    global restart

    start = Toplevel()

    start.configure(background='light blue')

    start.title("Teste - Projeto Integrador")

    start.geometry("1268x766")

    start.resizable(False, False)

    # BOTÃO DE LOGOUT

    logout = Button(start, text="Histórico de peso", bg='light blue', command=graficos)
    logout.place(x=1100, y=30)

    # relógio simples
    def clock():
        hour = datetime.datetime.now().strftime("%d/%m/%y   -  %H:%M:%S - %p")
        relogio.config(text=hour)
        relogio.after(1000, clock)

    relogio = Label(start, font=('Calibri', 12, 'bold'), bg="light blue")
    relogio.place(x=1050, y=700)
    clock()

    ####################################################################################################################

    # Auxiliar de coordenadas

    def motion(event):
        x, y = event.x, event.y
        print('x={}, y={}'.format(x, y))

    start.bind('<Button-1>', motion)

    ####################################################################################################################

    usuario = usuario_verify
    senha = senha_verify.get()

    # USUARIO LABEL E CARGO

    user = Label(start, text="Usuário: " + str(usuario.get()), font=("Arial", 10, 'bold'), bg="light blue")
    user.place(x=15, y=700)

    global inputValue
    global obs
    global obss

    obss = StringVar()
    obs = Entry(start)
    obs.place(x=265, y=300, width=300, height=20)

    obs_label = Label(start, text="O que deseja procurar ? ", bg="light blue")
    obs_label.place(x=85, y=300)




########################################################################################################################

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def destroy_windows():
    start.destroy()


def registro():
    global usuario
    global senha
    global usuario_entry
    global senha_entry
    global register_screen
    global usuario

    register_screen = Toplevel()
    register_screen.title("Registrar-se")
    register_screen.geometry("400x400")

    usuario = StringVar()
    senha = StringVar()

    Label(register_screen, text="Coloque as informações necessárias", bg="white").pack()
    Label(register_screen, text="").pack()

    usuario_label = Label(register_screen, text="Usuario *")
    usuario_label.pack()

    usuario_entry = Entry(register_screen, textvariable=usuario)
    usuario_entry.pack()

    senha_label = Label(register_screen, text="Senha *")
    senha_label.pack()

    senha_entry = Entry(register_screen, textvariable=senha, show='*')
    senha_entry.pack()

    Label(register_screen, text="").pack()

    Button(register_screen, text="Registrar", width=10, height=1, bg="white", command=cadastro_usuario).pack()


def cadastro_usuario():
    global usuario_info
    global senha_info
    global cargo_info

    usuario_info = usuario.get()
    senha_info = senha.get()

    file = open(usuario_info, "w")

    file.write(usuario_info + "\n")
    file.write(senha_info)
    file.close()

    usuario_entry.delete(0, END)
    senha_entry.delete(0, END)

    Label(register_screen, text="Registrado com sucesso!", fg="green", font=("Calibri", 11)).pack()
    Label(register_screen, text="Feche esta janela", fg="blue", font=("Calibri", 11)).pack()


def login_main():
    global login_main_screen

    login_main_screen = Toplevel()
    login_main_screen.geometry("300x250")
    login_main_screen.title("Faça Login em sua conta")
    Label(login_main_screen, text="Por Favor, coloque seus dados abaixo").pack()
    Label(login_main_screen, text="").pack()

    global usuario_verify
    global senha_verify

    usuario_verify = StringVar()
    senha_verify = StringVar()

    Label(login_main_screen, text="Usuário *").pack()
    usuario_login_entry = Entry(login_main_screen, textvariable=usuario_verify)
    usuario_login_entry.pack()

    Label(login_main_screen, text="").pack()
    Label(login_main_screen, text="Senha *").pack()

    senha_login_entry = Entry(login_main_screen, show='*', textvariable=senha_verify)
    senha_login_entry.pack()
    Label(login_main_screen, text="").pack()
    Button(login_main_screen, text="Login", width=10, height=1, command=login_verification).pack()


def login_verification():
    login_verify()


def login_verify():
    global login_verify

    usuario = usuario_verify.get()
    senha = senha_verify.get()

    list_of_files = os.listdir()
    if usuario in list_of_files and senha in list_of_files:
        file = open(usuario, "r")
        verify = file.read().splitlines()
        login_success()

    else:
        password_error()


def login_success():
    global login_success_screen

    login_success_screen = Toplevel()
    login_success_screen.title("Login")
    login_success_screen.geometry("200x200")
    Label(login_success_screen, text="Login efetuado com sucesso").pack()
    Button(login_success_screen, text="OK", command=delet_login_success).pack()

    start()


def delet_login_success():
    login_success_screen.destroy()
    login_main_screen.destroy()
    login_screen.withdraw()


def password_error():
    global password_error
    global password_error_screen

    password_error_screen = Toplevel()
    password_error_screen.title("Erro")
    password_error_screen.geometry("150x100")
    Label(password_error_screen, text="Senha inválida").pack()
    Button(password_error_screen, text="Ok", command=delete_password_error).pack()


def delete_password_error():
    password_error_screen.destroy()


def user_error():
    global user_error
    global user_error_screen

    user_error_screen = Toplevel()
    user_error_screen.title("Erro")
    user_error_screen.geometry("150x100")
    Label(user_error_screen, text="usuário inválido").pack()
    Button(user_error_screen, text="Ok", command=delete_user_error).pack()


def delete_user_error():
    user_error_screen.destroy()


def login():
    global login_screen
    # Cria a tela de Login
    login_screen = Tk()
    login_screen.geometry('400x400')
    login_screen.title("Login")
    Label(text="Faça seu Login, ou registre-se agora", bg="white", width="30").pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login_main).pack()
    Label(text="").pack()
    Button(text="Registrar-se", height="2", width="30", command=registro).pack()
    login_screen.mainloop()

########################################################################################################################

login()
