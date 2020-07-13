from tkinter import *
import threading
import tkinter.messagebox as MessageBox
import datetime
import recognizer
import pymysql as mysql
import pyttsx3


def speech():
    label2audio = ('Qual o dia do evento?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()


def speechHora():
    label2audio = ('Qual a hora do evento?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()


def speechTipo():
    label2audio = ('Qual o tipo do evento?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()


def speechDescricao():
    label2audio = ('Qual a descrição para o evento?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()


def speechBanco():
    label2audio = ('Operação confirmada com sucesso')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()


def speechConfirma():
    label2audio = ('Deseja comfirmar? \n Sim ou não?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()


def validaDataEvento(entrada):
    global valorDataEvento
    valorDataEvento = ""
    dataEvento = None

    meses = {'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
             'setembro': 9,
             'outubro': 10, 'novembro': 11, 'dezembro': 12}

    try:
        print("Entrada:", entrada)
        entradaDado = entrada.split(' ')  # 29 do 4 de 2002: vai separar por espaços
        dia = int(entradaDado[0])
        mes = entradaDado[2]
        ano = int(entradaDado[4])

        if mes.lower() not in meses.keys():
            print("Mês inexistente!")
            entDataEvento['text'] = 'Mês Inexistente'
            entDataEvento['bg'] = '#FF6347'
            return False

        if dia < 1 or dia > 31:
            print("O dia precisa ser entre 1 e 31!")
            entDataEvento['text'] = 'O dia precisa ser entre 1 e 31!'
            entDataEvento['bg'] = '#FF6347'
            return False

        mes = meses[mes]

        if mes < 1 or mes > 12:
            print("O mês precisa ser entre 1 e 12!")
            entDataEvento['text'] = 'O mês precisa ser entre 1 e 12!'
            entDataEvento['bg'] = '#FF6347'
            return False

        ano_atual = int(datetime.datetime.now().strftime("%Y"))
        if ano < ano_atual:
            print("Você não pode fazer lembretes no passado!")
            entDataEvento['text'] = 'Você não pode fazer lembretes no passado!'
            entDataEvento['bg'] = '#FF6347'
            return False

        dadosData = (str(ano), str(mes), str(dia))
        dadosDataFormat = (str(dia), str(mes), str(ano))
        data = "-".join(dadosData)
        dataFormat = "/".join(dadosDataFormat)
        print(data)
        print(f'O Número informado foi {data}')

        entDataEvento['text'] = dataFormat  # Valor que faz a mudança na label em tela.
        entDataEvento['bg'] = '#90EE90'
        valorDataEvento = data  # Valor a ser inserido no banco
        speechHora()
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entDataEvento['text'] = 'Valor inválido, repita'
        entDataEvento['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entDataEvento['text'] = 'Valor não foi dito corretamente.'
        entDataEvento['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entDataEvento['text'] = 'Valor inválido'
        entDataEvento['bg'] = '#FF6347'


def validaHoraEvento(entrada):
    global valorHoraEvento
    valorHoraEvento = ""
    horaEvento = None

    try:
        # hh:mm
        entrada_s = entrada.split(' ')
        if len(entrada_s) == 2 and entrada_s[1].lower() == 'horas':
            horas = [entrada_s[0], '00']
        else:
            horas = entrada.split(':')

        hora = int(horas[0])
        minuto = int(horas[1])

        if hora < 0 or hora > 23:
            return False

        if minuto < 0 or minuto > 59:
            return False

        hora_min = ":".join(horas)

        print('O Número informado foi {}'.format(hora_min))

        entHoraEvento['text'] = hora_min
        entHoraEvento['bg'] = '#90EE90'
        valorHoraEvento = hora_min
        speechTipo()
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entHoraEvento['text'] = 'Valor inválido, repita'
        entHoraEvento['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entHoraEvento['text'] = 'Valor não foi dito corretamente.'
        entHoraEvento['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entHoraEvento['text'] = 'Valor inválido'
        entHoraEvento['bg'] = '#FF6347'


def validaTipoEvento(entrada):
    print("Entrada: '{}'".format(entrada))
    global valorTipoEvento
    valorTipoEvento = 0
    tipoEvento = None

    tipos_alerta = {'vacina': 1, 'banho': 2, 'outros': 3}

    try:
        tipoEvento = entrada
        print("O tipo de evento mencionado é: ", tipoEvento.title())
        if tipoEvento.lower() in tipos_alerta.keys():
            valorTipoEvento = tipos_alerta[tipoEvento.lower()]
        else:
            print('Valor não foi dito corretamente.')
            entTipoEvento['text'] = 'Valor não foi dito corretamente.'
            entTipoEvento['bg'] = '#FF6347'
            return False

        entTipoEvento['text'] = tipoEvento.title()
        entTipoEvento['bg'] = '#90EE90'
        speechDescricao()
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entTipoEvento['text'] = 'Valor inválido, repita'
        entTipoEvento['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entTipoEvento['text'] = 'Valor não foi dito corretamente.'
        entTipoEvento['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entTipoEvento['text'] = 'Valor inválido'
        entTipoEvento['bg'] = '#FF6347'


def validaDescricaoEvento(entrada):
    global valorDescEvento
    valorDescEvento = ''
    descricaoEvento = None
    try:
        descricaoEvento = entrada

        if descricaoEvento == '':
            entDescricaoEvento['text'] = 'Insira a descrição!'
            entDescricaoEvento['bg'] = '#FF6347'
            return False
        print("Descrição do seu evento: ", descricaoEvento.upper())
        entDescricaoEvento['text'] = descricaoEvento.upper()
        entDescricaoEvento['bg'] = '#90EE90'
        valorDescEvento = descricaoEvento.upper()
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
        entDescEvento['text'] = 'Valor inválido'
        entDescEvento['bg'] = '#FF6347'


# Função para validar e sair da tela em questão.
def valida():
    #    return True
    confirmado = False
    while confirmado is not True:
        # Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
        campos = {
            'Data do evento': {'validacao': validaDataEvento, 'mensagem': 'Quando será o dia do evento?'},
            'Hora do evento': {'validacao': validaHoraEvento, 'mensagem': 'Qual será o horário do evento?'},
            'Tipo do evento': {'validacao': validaTipoEvento, 'mensagem': 'Qual o tipo do evento (Vacina/ Banho/ '
                                                                          'Outros)?'},
            'Descrição do evento': {'validacao': validaDescricaoEvento, 'mensagem': 'Diga uma breve descrição do '
                                                                                    'evento: '}
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
                    print('Deseja confirmar? \n Sim ou Não?')
                    speechConfirma()
                    texto = recognizer.recognizer()
                    if texto.lower() == 'não' or texto.lower() == 'sim':
                        confirmado_valido = True
                        if texto.lower() == 'sim':
                            valido = True
                            confirmado = True
                            speechBanco()
                            insertCrud()
                            janela.after(1000, lambda: janela.destroy())
                        else:
                            entDataEvento['text'] = "Falar ex: 26 do Junho de 2000"
                            entHoraEvento['text'] = "Falar ex: 10 e 15 (10 para horas e 15 para minutos)"
                            entTipoEvento['text'] = "Tipos disponíveis: Vacina/ Banho/ Outros"
                            entDescricaoEvento['text'] = "Fale uma breve descrição do evento"
                            entDataEvento['bg'] = "white"
                            entHoraEvento['bg'] = "white"
                            entTipoEvento['bg'] = "white"
                            entDescricaoEvento['bg'] = "white"
                            speech()
        print('Saiu')


def insertCrud():
    print(valorHoraEvento)

    datetimeAfter = (valorDataEvento, valorHoraEvento)

    datetime = " ".join(datetimeAfter)

    print(datetime)

    mydb = mysql.connect(host='localhost', user='root', password='', db='mydb', charset='utf8mb4')

    cursor = mydb.cursor(mysql.cursors.DictCursor)

    cursor.execute('insert into alerta (data_alerta, descricao_alerta, id_dono, id_tipo_alerta, situacao) '
                   'values ("' + datetime + '","' + str(valorDescEvento) + '", 2, ' + str(valorTipoEvento) + ', 1)')

    cursor.execute("commit");

    MessageBox.showinfo("Status da ação", "Dados inseridos com sucesso");

    mydb.close()


t = threading.Thread(name='my_service', target=valida)
t.start()

# ========================== JANELA TKINTER ========================== #
# def registro_racao():
janela = Tk()
janela.geometry("350x500+500+200")
janela.wm_title("Assistente Pet")
lblTitulo = Label(janela, text="REGISTRO DE LEMBRETES", font=("Arial", 10, "bold")).place(x=80, y=10)

# ===================== VARIAVEIS LOCAIS E GLOBAIS ===================== #
global entDataEvento
global entHoraEvento
global entTipoEvento
global entDescricaoEvento
entDataEvento = StringVar()
entHoraEvento = StringVar()
entTipoEvento = StringVar()
entDescricaoEvento = StringVar()

# Labels de idenficação dos campos
lblData = Label(janela, text="Dia do evento:", font=("Arial", 10, "bold")).place(x=10, y=50)
lblHora = Label(janela, text="Hora do evento:", font=("Arial", 10, "bold")).place(x=10, y=130)
lblTipo = Label(janela, text="Qual é o tipo do evento:", font=("Arial", 10, "bold")).place(x=10, y=210)
lblDescricao = Label(janela, text="Uma descrição para o evento:", font=("Arial", 10, "bold")).place(x=10, y=290)

# Labels que aparecerão as respostas para nome e tipo do pet
entDataEvento = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Falar ex: 26 de julho de 2000")
entDataEvento.place(x=10, y=80)

entHoraEvento = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Falar ex: 10 e 15 (10 "
                                                                                           "para horas e 15 para minutos)")
entHoraEvento.place(x=10, y=160)

entTipoEvento = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Tipos disponíveis: "
                                                                                           "Vacina/ Banho/ Outros")
entTipoEvento.place(x=10, y=240)

entDescricaoEvento = Label(janela, font=("Arial", 10), bg='white', width='40', height='2',
                           text="Fale uma breve descrição do evento")
entDescricaoEvento.place(x=10, y=320)

t = threading.Thread(target=speech)
t.start()

janela.mainloop()