from tkinter import *
import threading
import tkinter.messagebox as MessageBox
from datetime import date
import datetime
import recognizer
import crud
import pymysql as mysql
import pyttsx3

# ======================= FUNCOES DO SISTEMA ======================== #

def speech():
    label2audio = ('Qual a marca da ração?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def speechQuantia():
    label2audio = ('Qual a quantia total do saco de ração?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def speechDiario():
    label2audio = ('Qual o valor diário de ração entregue ao pet?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def speechBanco():
    label2audio = ('Operação confirmada com sucesso')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def speechConfirma():
    label2audio = ('Deseja comfirmar? Sim ou não')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def validaMarcaRacao(entrada):
    global valorMarcaRacao
    valorMarcaRacao = str('')
    marcaRacao = None
    try:

        if entrada == '':
            entMarcaRacao['text'] = 'Insira o Marca da Ração!'
            entMarcaRacao['bg'] = '#FF6347'
            return False
        marcaRacao = entrada
        print("A marca de ração mencionada foi: ", marcaRacao.title())
        entMarcaRacao['text'] = marcaRacao.title()
        entMarcaRacao['bg'] = '#90EE90'
        valorMarcaRacao = marcaRacao.title()
        speechQuantia()
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entMarcaRacao['text'] = 'Valor inválido, repita'
        entMarcaRacao['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entMarcaRacao['text'] = 'Valor não foi dito corretamente.'
        entMarcaRacao['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entMarcaRacao['text'] = 'Valor inválido'
        entMarcaRacao['bg'] = '#FF6347'


def validaSacoRacao(entrada):
    global valorSacoRacao
    valorSacoRacao = float(0)
    racaoPct = None
    try:
        if entrada == '':
            entSacoRacao['text'] = 'Insira o Marca da Ração!'
            entSacoRacao['bg'] = '#FF6347'
            return False
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
        racaoPct = float(numero)
        entSacoRacao['text'] = '{:.3f}'.format(racaoPct)
        entSacoRacao['bg'] = '#90EE90'
        valorSacoRacao = '{:.3f}'.format(racaoPct)
        speechDiario()
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entSacoRacao['text'] = 'Valor inválido, repita'
        entSacoRacao['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entSacoRacao['text'] = 'Valor não foi dito corretamente.'
        entSacoRacao['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entSacoRacao['text'] = 'Valor inválido'
        entSacoRacao['bg'] = '#FF6347'


def validaRacaoDiaria(entrada):
    global valorRacaoDia
    valorRacaoDia = float(0)
    racaoDia = None
    try:
        entradaDado = entrada.split()
        if len(entradaDado) == 3:
            valor1 = entradaDado[0]
            valor2 = entradaDado[2]
            valor = (valor1, valor2)
            numero = ".".join(valor)
        elif len(entradaDado) == 4:
            valor1 = entradaDado[0]
            valor2 = entradaDado[2]
            valor = (valor1, valor2)
            numero = ".".join(valor)
        elif len(entradaDado) == 5:
            valor1 = entradaDado[0]
            valor2 = entradaDado[3]
            valor = (valor1, valor2)
            numero = ".".join(valor)
        else:
            valor1 = ['0',entradaDado[0]]
            numero = ".".join(valor1)

        print('O Número informado foi:', numero)
        racaoDia = float(numero)
        entRacaoDiario['text'] = '{:.3f}'.format(racaoDia)
        entRacaoDiario['bg'] = '#90EE90'
        valorRacaoDia = '{:.3f}'.format(racaoDia)
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entRacaoDiario['text'] = 'Valor inválido, repita'
        entRacaoDiario['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entRacaoDiario['text'] = 'Valor não foi dito corretamente.'
        entRacaoDiario['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entRacaoDiario['text'] = 'Valor inválido'
        entRacaoDiario['bg'] = '#FF6347'


# Função para validar e sair da tela em questão.
def valida():
#    return True
    confirmado = False
    while confirmado is not True:
        # Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
        campos = {
            'Marca Ração': {'validacao': validaMarcaRacao, 'mensagem': 'Qual a marca da ração comprada?'},
            'Saco de Ração': {'validacao': validaSacoRacao, 'mensagem': 'Qual o peso do saco de ração comprado?'},
            'Racao Diaria': {'validacao': validaRacaoDiaria, 'mensagem': 'Qual o valor de ração diário entregue ao pet?'}
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
                    speechConfirma()
                    texto = recognizer.recognizer()
                    if texto.lower() == 'sim' or texto.lower() == 'não':
                        confirmado_valido = True
                        if texto.lower() == 'sim':
                            valido = True
                            confirmado = True
                            speechBanco()
                            insertCRUD()
                            janela.after(5000, lambda: janela.destroy())
                        else:
                            entMarcaRacao['text'] = "Qual a marca da ração comprada?"
                            entSacoRacao['text'] = "Qual o peso do saco de ração comprado?"
                            entRacaoDiario['text'] = "Qual o valor de ração diário entregue ao pet?"
                            entMarcaRacao['bg'] = "white"
                            entSacoRacao['bg'] = "white"
                            entRacaoDiario['bg'] = "white"
                            speech()
            print('Saiu')


def insertCRUD():
    hoje = date.today()
    if str(valorMarcaRacao)=="" or valorSacoRacao=="" or valorRacaoDia=="":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        #Insert na tabela ração
        nome_tabela = 'racao'
        dados = {'marca_racao': valorMarcaRacao, 'quant_racao': valorSacoRacao, 'quant_diaria_racao': valorRacaoDia,
             'data_compra_racao': hoje}
        crud.insert(nome_tabela, dados)

        #Cálculo de alerta
        quant_racao = float(dados['quant_racao'])
        quant_racao_diaria = float(dados['quant_diaria_racao'])

        dias_duracao = int((quant_racao/quant_racao_diaria)-1)
        dias_duracao = datetime.timedelta(days = dias_duracao)
        previsao_acabar = hoje + dias_duracao

        # Insert na tabela de alerta para mandar as notificações
        nome_tabela = 'alerta'
        dados = {'data_alerta': previsao_acabar, 'id_dono': 2, 'id_tipo_alerta': 4, 'situacao': 1,
                 'descricao_alerta': 'Alerta de Ração'}
        crud.insert(nome_tabela, dados)

t = threading.Thread(name='my_service', target=valida)
t.start()


# ========================== JANELA TKINTER ========================== #
janela = Tk()
janela.geometry("350x500+500+200")
janela.wm_title("Assistente Pet")
lblTitulo = Label(janela, text="REGISTRO DE RAÇÃO DO PET", font=("Arial", 10, "bold")).place(x=70, y=10)

# ===================== VARIAVEIS LOCAIS E GLOBAIS ===================== #
global entMarcaRacao
global entSacoRacao
global entRacaoDiario
entMarcaRacao = StringVar()
entSacoRacao = StringVar()
entRacaoDiario = StringVar()

# Labels de idenficação dos campos
lblMarcaRacao = Label(janela, text="Qual a marca da ração:", font=("Arial", 10, "bold")).place(x=10, y=50)
lblSacoRacao = Label(janela, text="Quantia total do saco de ração:", font=("Arial", 10, "bold")).place(x=10, y=130)
lblValorDia = Label(janela, text="Valor diário de ração dada ao pet :", font=("Arial", 10, "bold")).place(x=10, y=210)

# Labels que aparecerão as respostas para nome e tipo do pet
#entMarcaRacao = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', textvariable=txtMarcaRacao)
entMarcaRacao = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Qual a marca da ração?")
entMarcaRacao.place(x=10, y=80)
#entSacoRacao = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', textvariable=txtSacoRacao)
entSacoRacao = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Qual o peso do saco de "
                                                                                          "ração comprado?")
entSacoRacao.place(x=10, y=160)
#entRacaoDiario = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', textvariable=txtRacaoDia)
entRacaoDiario = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Qual o valor de ração diário entregue ao pet?")
entRacaoDiario.place(x=10, y=240)

t = threading.Thread(target=speech)
t.start()

janela.mainloop()