from tkinter import *
import threading
import tkinter.messagebox as MessageBox
from datetime import date
import recognizer
import crud
import pymysql as mysql

# ======================= FUNCOES DO SISTEMA ======================== #
def validaPesoPet(entrada):
    global valorPesoPet
    valorPesoPet = float(0)
    pesoKgPet = None
    try:
        entradaDado = entrada.split()
        if len(entradaDado) == 3:
            valor01 = entradaDado[0]
            valor02 = entradaDado[2]
            valores = (valor01, valor02)
            numero = ".".join(valores)
        elif len(entradaDado) == 4:
            valor01 = entradaDado[0]
            valor02 = entradaDado[2]
            valores = (valor01, valor02)
            numero = ".".join(valores)
        elif len(entradaDado) == 5:
            valor01 = entradaDado[0]
            valor02 = entradaDado[3]
            valores = (valor01, valor02)
            numero = ".".join(valores)
        else:
            numero = entradaDado[0]

        print(f'O Número informado foi {numero}')
        pesoKgPet = float(numero)
        entPeso['text'] = '{:.3f}'.format(pesoKgPet)
        valorPesoPet = '{:.3f}'.format(pesoKgPet)
        entPeso['bg'] = '#90EE90'
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entPeso['text'] = 'Valor inválido, repita'
        entPeso['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entPeso['text'] = 'Valor não foi dito corretamente.'
        entPeso['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entPeso['text'] = 'Valor inválido'
        entPeso['bg'] = '#FF6347'

def validaNomePet(entrada):
    global nomePet
    valorNomePet = ''
    nome = None
    try:
        nome = entrada

        if entrada == '':
            entNomePet['text'] = 'Insira o Nome!'
            entNomePet['bg'] = '#FF6347'
            return False
        print("Nome do Pet: ", nome.upper())
        entNomePet['text'] = nome.upper()
        entNomePet['bg'] = '#90EE90'
        valorNomePet = nome.upper()
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entNomePet['text'] = 'Valor inválido, repita'
        entNomePet['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entNomePet['text'] = 'Valor não foi dito corretamente.'
        entNomePet['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entNomePet['text'] = 'Valor inválido'
        entNomePet['bg'] = '#FF6347'


def insertCRUD():
    hoje = date.today()
    print(hoje)

    if valorPesoPet == "":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        nome_tabela = 'hist_peso'
        dados = {'peso': valorPesoPet, 'data': hoje, 'pet_id_pet': 2}
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
        confirmado = False
        while confirmado is not True:
            for campo in campos.keys():
                valido = False
                while valido is not True:
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
                confirmado_valido = False
                while confirmado_valido is not True:
                    print('Deseja confirmar sim ou não')
                    texto = recognizer.recognizer()
                    if texto.lower() == 'sim' or texto.lower() == 'não':
                        confirmado_valido = True
                        if texto.lower() == 'sim':
                            valido = True
                            confirmado = True
                            insertCRUD()
                            janela.after(5000, lambda: janela.destroy())
                        else:
                            entPeso['text'] = "Diga o peso do pet, ex: 12 Kg e 500 gramas"
                            entNomePet['text'] = "Diga o nome do pet"
                            entPeso['bg'] = "white"
                            entNomePet['bg'] = "white"
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