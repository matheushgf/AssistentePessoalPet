from tkinter import *
import threading
import tkinter.messagebox as MessageBox
from datetime import date
from petassistant_develop import recognizer
from petassistant_develop import crud


# ======================= FUNCOES DO SISTEMA ======================== #
def validaMarcaRacao(entrada):
    global valorMarcaRacao
    valorMarcaRacao = ''
    marcaRacao = None
    try:
        marcaRacao = entrada
        print("A marca de ração mencionada foi: ", marcaRacao.title())
        entMarcaRacao['text'] = marcaRacao.title()
        valorMarcaRacao = marcaRacao.title()
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')


def validaSacoRacao(entrada):
    global valorSacoRacao
    valorSacoRacao = float(0)
    racaoPct = None

    try:
        entradaDado = entrada.split(' ')
        numero = entradaDado[0]
        print(entradaDado)
        print(f'O Número informado foi {numero}')
        numero = numero.replace(',', '.')
        racaoPct = float(numero)
        entSacoRacao['text'] = '{:.3f}'.format(racaoPct)
        valorSacoRacao = '{:.3f}'.format(racaoPct)
        print(valorSacoRacao)
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')


def validaRacaoDiaria(entrada):
    global valorRacaoDia
    valorRacaoDia = float(0)
    racaoDia = None

    try:
        entradaDado = entrada.split(' ')
        numero = entradaDado[0]
        print(entradaDado)
        print(f'O Número informado foi {numero}')
        numero = numero.replace(',', '.')
        racaoDia = float(numero)
        entRacaoDiario['text'] = '{:.3f}'.format(racaoDia)
        valorRacaoDia = '{:.3f}'.format(racaoDia)
        print(valorRacaoDia)
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')


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
                    print(valorMarcaRacao)
                    print(valorSacoRacao)
                    print(valorRacaoDia)
                    insertcrud()
                    janela.after(5000, lambda: janela.destroy())
                else:
                    entMarcaRacao['text'] = "Qual a marca da ração comprada?"
                    entSacoRacao['text'] = "Qual o peso do saco de ração comprado?"
                    entRacaoDiario['text'] = "Qual o valor de ração diário entregue ao pet?"
    print('Saiu')


def insertcrud():
    hoje = date.today()
    print(hoje)

    if str(valorMarcaRacao)=="" or valorSacoRacao=="" or valorRacaoDia=="":
        MessageBox.showinfo("Campos em branco! Favor preencher os requisitos")
    else:
        nome_tabela = 'racao'
        dados = {'marca_racao': valorMarcaRacao, 'quant_racao': valorSacoRacao, 'quant_diaria_racao': valorRacaoDia,
             'data_compra_racao': hoje}
        crud.insert(nome_tabela, dados)


t = threading.Thread(name='my_service', target=valida)
t.start()


# ========================== JANELA TKINTER ========================== #
#def registro_racao():
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

# txtMarcaRacao.set("Qual a marca da ração?")
# txtSacoRacao.set("Qual o peso do saco de ração comprado?")
# txtRacaoDia.set("Qual o valor de ração diário entregue ao pet?")

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

janela.mainloop()

#janela.after(5000,lambda:janela.destroy())
#registro_racao()
#_thread.start_new_thread(registro_racao())
#_thread(registro_racao())
#registro_racao()
