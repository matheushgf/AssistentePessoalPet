from tkinter import *

root = Tk()
root.configure(background='light blue')
root.title("Mapa para pets")
root.geometry('500x500')
T = Label(root, bg="light blue", text="Mapa com marcação dos locais que aceitam pets")
T.config(font=("Helvetica", 12))
T.place(x=250, y=200)

# Adicionar label para pesquisa de itens no Mapa, como exemplo Veterinário
Ep = Label(root, bg="light blue", text="Pesquisar: ", font="Helvetica")
Ep.place(x=10, y=30)
E = Entry(root, font="Helvetica", width=40)
E.place(x=100, y=30)

# Adicionar Mapa Google Maps


# Adicionar processo de pesquisa no mapa e localização
# Caso mapa estático apenas informar pins com locais


Close = Button(root, anchor="w", text="Fechar", bg="light blue", command=root.destroy)
Close.place(x=50, y=450)

T.pack()
root.mainloop()