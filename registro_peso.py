from tkinter import *
import threading
import tkinter.messagebox as MessageBox
from datetime import date
from petassistant_feature.pet_interfacegrafica import recognizer
from petassistant_feature.pet_bd import crud
import mysql

# ======================= FUNCOES DO SISTEMA ======================== #
def validaPesoPet(entrada):
    global valorPesoPet
    valorPesoPet = ''
    pesoKgPet = None
    try:
        entradaDado = entrada.split(' ')
        kilos = entradaDado[0]
        gramas = entradaDado[3]
        pesointeiro = (kilos, gramas)
        pesoKgPet = ".".join(pesointeiro)
        print(pesoKgPet)
        entPeso['text'] = pesoKgPet
        valorPesoPet = pesoKgPet
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')

def validaNomePet(entrada):
    global nomePet
    nomePet = None
    try:
        nomePet = entrada
        print("Nome do pet informado: ", nomePet.title())
        entNomePet['text'] = nomePet.title()
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')


'''
def selectCRUD(nome):
    global resultado
    resultado = ''

    mydb = mysql.connect(host='127.0.0.1', user='petuser', password='', db='mydb', charset='utf8mb4')
    cursor = mydb.cursor(mysql.cursors.DictCursor)
    resultado = cursor.execute("SELECT id_tipo_pet FROM pet WHERE nome_pet=%s", nome)
    cursor.execute("commit");
    mydb.close()
    print(resultado)

'''


def insertCRUD():
    hoje = date.today()
    print(hoje)

    if valorPesoPet == "":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        nome_tabela = 'hist_peso'
        dados = {'peso': valorPesoPet, 'data': hoje, 'pet_id_pet': 14}
        crud.insert(nome_tabela, dados)


# Função para validar e sair da tela em questão.
def valida():
    confirmado = False
    while confirmado is not True:
        # Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
        campos = {
            'Peso do Pet': {'validacao': validaPesoPet, 'mensagem': 'Qual o peso do seu Pet?'},
            'Nome do Pet': {'validacao': validaNomePet, 'mensagem': 'Qual o nome do pet?'}}

#       Laço para percorrer todos os campos pela ordem da chave.
        valido = False
        while valido is not True:
            for campo in campos.keys():
                # Seleção do campo.
                dados = campos[campo]
                print(dados['mensagem'])
                # mensagem(dados['mensagem'])
                texto = recognizer.recognizer()

#               Validação do comando dito.
                try:
                    metodo = dados['validacao']
                    valido = metodo(texto)
                except:
                    print('Erro no método de validação')
                    break

#           Validação dos dados para sair da tela.
            if valido:
                print('Deseja confirmar sim ou não')
                texto = recognizer.recognizer()
                if texto.lower() == 'sim':
                    valido = True
                    confirmado = True
                    print(valorPesoPet)
                    insertCRUD()
                    janela.after(5000, lambda: janela.destroy())
                else:
                    entPeso['text'] = "Diga o peso do pet, ex: 12 Kg e 500 gramas"
                    entNomePet['text'] = "Diga o nome do pet"
    print('Saiu')


t = threading.Thread(name='my_service', target=valida)
t.start()


# ========================== JANELA TKINTER ========================== #
janela = Tk()
janela.geometry("350x500+500+200")
janela.wm_title("Assistente Pet")
lblTitulo = Label(janela, text="REGISTRO DE PESO DO PET", font=("Arial", 10, "bold")).place(x=70, y=10)


# ===================== VARIAVEIS LOCAIS E GLOBAIS ===================== #
global entPeso
entPeso = StringVar()
global entNomePet
entNomePet = StringVar()

# Labels de idenficação dos campos
lblPeso = Label(janela, text="Qual o peso do pet:", font=("Arial", 10, "bold")).place(x=10, y=50)
#lblNomePet = Label(janela, text="Qual o nome do pet:", font=("Arial", 10, "bold")).place(x=10, y=130)

# Labels que aparecerão as respostas
entPeso = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Diga o peso do pet, ex: 12 Kg e 500 gramas")
entPeso.place(x=10, y=80)
entNomePet = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Diga o nome do pet")
entNomePet.place(x=10, y=160)

janela.mainloop()