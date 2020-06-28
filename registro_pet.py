from tkinter import *
import threading
import tkinter.messagebox as MessageBox
from petassistant_develop import recognizer
from petassistant_develop import crud

# ---------------------------- FUNÇÕES DO CADASTRO ---------------------------- #
#Validação dos dados recebidos pelo laço valida()
def validaNomePet(entrada):
    global valorNomePet
    valorNomePet = ''
    nomePet = None
    try:
        nomePet = entrada
        print("Descrição do seu evento: ", nomePet.title())
        entNomePet['text'] = (nomePet.title())
        valorNomePet = (nomePet.title())
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')


def validaTipoPet(entrada):
    global valorTipoPet
    valorTipoPet = ''
    tipoPet = None
    try:
        tipoPet = entrada
        print("A marca de ração mencionada foi: ", tipoPet.title())
        entTipoPet['text'] = tipoPet.title()
        if tipoPet.lower() == 'cachorro':
            valorTipoPet = 1
        elif tipoPet.lower == 'gato':
            valorTipoPet = 2
        else:
            valorTipoPet = 3
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')


#Laço de repeticação que irá perguntar sobre os intens em tela e irá chamar as funçõe responsáveis para tratamento.
def valida():
    confirmado = False
    while confirmado is not True:
        # Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
        campos = {
            'Nome do pet': {'validacao': validaNomePet, 'mensagem': 'Qual o nome do seu pet?'},
            'Tipo do pet': {'validacao': validaTipoPet, 'mensagem': 'Qual é o tipo do seu pet?'}
        }

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
                    if texto.lower() == 'não' or texto.lower() == 'sim':
                        confirmado_valido = True
                        if texto.lower() == 'sim':
                            valido = True
                            confirmado = True
                            insertCRUD()
                            janela.after(5000, lambda: janela.destroy())
                        else:
                            entNomePet['text'] = "Qual o nome do seu pet?"
                            entTipoPet['text'] = "Que tipo é o pet?"
        print('Saiu')


# CRUD para inserir dados no banco após validados
def insertCRUD():
    if valorNomePet=="" or valorTipoPet=="":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        nome_tabela = 'pet'
        dados = {'nome_pet': valorNomePet, 'id_tipo_pet': valorTipoPet}
        crud.insert(nome_tabela, dados)

# Thread para rodar duas ações ao mesmo tempo.
t = threading.Thread(name='my_service', target=valida)
t.start()


# ------------------------------ TKINTER INTERFACE ------------------------------ #
janela = Tk()
janela.geometry("350x500+500+200")
janela.wm_title("Assistente Pet")
lbltitulo = Label(janela, text="REGISTRO DO PET", font=("Arial", 10, "bold")).place(x=110, y=10)

# ===== VARIAVEIS LOCAIS ===== #
global entNomePet
global entTipoPet
entNomePet = StringVar()
entTipoPet = StringVar()

# Labels de idenficação dos campos
lblnome = Label(janela, text="Nome do Pet:", font=("Arial", 10, "bold")).place(x=10, y=50)
lbltipo = Label(janela, text="Tipo do Pet:", font=("Arial", 10, "bold")).place(x=10, y=130)

# Labels que aparecerão as respostas para nome e tipo do pet
entNomePet = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text='Qual o nome do seu pet?')
entNomePet.place(x=10, y=80)
entTipoPet = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text='Que tipo é o pet?')
entTipoPet.place(x=10, y=160)

janela.mainloop()
