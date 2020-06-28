from tkinter import *
import threading
import tkinter.messagebox as MessageBox
import recognizer
import crud

# ---------------------------- FUNÇÕES DO CADASTRO ---------------------------- #
#Validação dos dados recebidos pelo laço valida()
def validaNomePet(entrada):
    global valorNomePet
    valorNomePet = ''
    nome = None
    try:
        nome = entrada

        if entrada == '':
            entNomePet['text'] = 'Insira o Nome!'
            entNomePet['bg'] = '#FF6347'
            return False
        print("Nome do Pet: ", nome.title())
        entNomePet['text'] = nome.title()
        entNomePet['bg'] = '#90EE90'
        valorNomePet = nome.title()
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entDescEvento['text'] = 'Valor inválido, repita'
        entDescEvento['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entDescEvento['text'] = 'Valor não foi dito corretamente.'
        entDescEvento['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entNomePet['text'] = 'Valor inválido'
        entNomePet['bg'] = '#FF6347'


def validaTipoPet(entrada):
    global valorTipoPet
    valorTipoPet = ''
    tipoPet = None

    tipos_pet = {'cachorro': 1, 'gato': 2, 'outros': 3}

    try:
        tipoPet = entrada
        print("A marca de ração mencionada foi: ", tipoPet.title())
        if tipoPet.lower() in tipos_pet.keys():
            entTipoPet['text'] = tipoPet.title()
            entTipoPet['bg'] = '#90EE90'
            valorTipoPet = tipos_pet[tipoPet.lower()]
        else:
            print('Valor não foi dito corretamente.')
            entTipoPet['text'] = 'Valor não foi dito corretamente.'
            entTipoPet['bg'] = '#FF6347'
            return False
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entTipoPet['text'] = 'Valor inválido, repita'
        entTipoPet['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entTipoPet['text'] = 'Valor não foi dito corretamente.'
        entTipoPet['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entTipoPet['text'] = 'Valor inválido'
        entTipoPet['bg'] = '#FF6347'


#Laço de repeticação que irá perguntar sobre os intens em tela e irá chamar as funçõe responsáveis para tratamento.
def valida():
    confirmado = False
    while confirmado is not True:
        # Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
        campos = {
            'Nome do pet': {'validacao': validaNomePet, 'mensagem': 'Qual o nome do seu pet?'},
            'Tipo do pet': {'validacao': validaTipoPet, 'mensagem': 'Qual é o tipo do seu pet?(Cachorro/Gato/Outros)'}
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
                            entNomePet['bg'] = "white"
                            entTipoPet['bg'] = "white"
        print('Saiu')


# CRUD para inserir dados no banco após validados
def insertCRUD():
    if valorNomePet=="" or valorTipoPet=="":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        nome_tabela = 'pet'
        dados = {'nome_pet': valorNomePet, 'id_tipo_pet': valorTipoPet, 'id_dono': 3}
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
entTipoPet = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text='Que tipo é o pet?(Cachorro/Gato/Outros)')
entTipoPet.place(x=10, y=160)

janela.mainloop()
