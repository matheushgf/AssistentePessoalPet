from tkinter import *
from tkinter import ttk
from datetime import date
from Teste_crud import crud


class Application:
    def __init__(self, master=None):
        
        #container 1: title_page
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.title_page = Label(self.widget1, text="Registro de Peso")
        self.title_page["font"] = ("Arial", "14", "bold")
        self.title_page.pack ()

        #container 2: lbl_peso e entry_peso
        self.widget2 = Frame(master)
        self.widget2.pack()

        self.lbl_peso = Label(self.widget2, text = "Insira o Peso do Pet(Kg):")
        self.lbl_peso["font"] = ("Arial", "12", "bold")
        self.lbl_peso.pack()

        self.entry_peso = Entry(self.widget2)
        self.entry_peso["font"] = ("Arial","12")
        self.entry_peso.pack()
        
        #container btn_send: send_res
        self.widget_send = Frame(master)
        self.widget_send.pack(side = BOTTOM)

        def send_reg ():

            peso = float(self.entry_peso.get())
            data = "{:%d/%m/%Y}".format(date.today())
            id_pet = 1

            crud = Crud()

            values = (peso, data, id_pet)

            print(values)

            crud.insert("hist_peso", values)
            

        self.btn_send = Button(self.widget_send, command = send_reg)
        self.btn_send["text"] = "Enviar"
        self.btn_send["font"] = ("Arial", "12")
        self.btn_send["width"] = 5
        self.btn_send.pack ()

        pass

window = Tk()

window.geometry("250x150")
window.title("Registro de Peso - Assistente Pessoal Pet")

Application(window)
window.mainloop()