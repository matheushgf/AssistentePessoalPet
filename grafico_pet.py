from tkinter import *
import threading
import matplotlib.pyplot as plt
from pylab import *
import pymysql as mysql
import recognizer
import os.path
import time
import pyttsx3

# ---------------------------- FUNÇÕES DO CADASTRO ---------------------------- #
# Validação dos dados recebidos pelo laço valida()

def speech():
    label2audio = ('Informe uma opção de tempo de gráfico: Semanal, Mensal ou Ano.')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def speechConfirma():
    label2audio = ('Deseja gerar outro grafico? Sim ou Não?')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()


def validaTempo(entrada):
    global sqlscript
    global valorTempo
    valorTempo = ''
    tempoGrafico = None

    try:
        tempoGrafico = entrada
        if entrada.lower() == 'semanal':
            print('Valor mencionado foi (s): ', entrada.title())
            entTempoGrafico['text'] = tempoGrafico.title()
            entTempoGrafico['bg'] = '#90EE90'
            sqlscript = 'SELECT * FROM mydb.hist_peso WHERE data BETWEEN curdate() - interval 7 day and curdate() ' \
                        'ORDER BY peso ASC'

        elif entrada.lower() == 'mensal':
            print('Valor mencionado foi (m): ', entrada.title())
            entTempoGrafico['text'] = tempoGrafico.title()
            entTempoGrafico['bg'] = '#90EE90'
            sqlscript = 'SELECT * FROM mydb.hist_peso WHERE month(data)=(month(now())-1) ORDER BY peso ASC'

        elif entrada.lower() == 'ano':
            print('Valor mencionado foi (a): ', entrada.title())
            entTempoGrafico['text'] = tempoGrafico.title()
            entTempoGrafico['bg'] = '#90EE90'
            sqlscript = 'SELECT * FROM mydb.hist_peso WHERE year(data)=(year(now())-1) ORDER BY peso ASC'

        else:
            entTempoGrafico['text'] = 'Informe um valor válido!'
            entTempoGrafico['bg'] = '#FF6347'
            return False
        return True
    except AttributeError:
        print('Valor inválido, repita')
        entTempoGrafico['text'] = 'Valor inválido, repita'
        entTempoGrafico['bg'] = '#FF6347'
    except ValueError:
        print('Valor não foi dito corretamente.')
        entTempoGrafico['text'] = 'Valor não foi dito corretamente.'
        entTempoGrafico['bg'] = '#FF6347'
    except:
        print('Valor inválido')
        entTempoGrafico['text'] = 'Valor inválido'
        entTempoGrafico['bg'] = '#FF6347'


def lerBanco(sqlscript):
    if os.path.isfile('grafico.png'):
        os.remove('grafico.png')

    eixoX = []
    eixoY = []
    c = mysql.connect(host='localhost', user='root', password='Admin001@', db='mydb', charset='utf8mb4')
    with c:
        mydb = c.cursor(mysql.cursors.DictCursor)
        print(sqlscript)
        mydb.execute(sqlscript)
        resultados = mydb.fetchall()
        print(resultados)
        for row in resultados:
            eixoX.append(row['data'])
            eixoY.append('{:.3f}'.format(row['peso']))

    subplots_adjust(bottom=.16, right=.97)
    # Cores nos eixos x e y
    tick_params(axis='x', colors='#072b57')
    tick_params(axis='y', colors='#072b57')
    xlabel('DATAS REGISTRADAS', color='#072b57')
    ylabel('ELEVAÇÃO PESO DO PET', color='#072b57')
    title('GRÁFICO HISTÓRICO DE PESO DO PET', color='#072b57')
    pos = arange(len(eixoX)) + .5
    bar(pos, eixoY, align='center', color='blue')
    xticks(pos, eixoX, rotation=30, size='small')
    grid(True)

    savefig('grafico.png')
    btnimage = PhotoImage(file='grafico.png')
    imagemGrafico = Label(janela, image=btnimage)
    imagemGrafico.image = btnimage
    imagemGrafico.place(x=5, y=155)
    time.sleep(10)
    return True

# Laço de repeticação que irá perguntar sobre os itens em tela e irá chamar as funçõe responsáveis para tratamento.
def valida():
    confirmado = False
    while confirmado is not True:
        # Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
        campos = {'Tempo do gráfico': {'validacao': validaTempo, 'mensagem': 'Qual o tempo desejado do gráfico?'}}

        #Laço para percorrer todos os campos pela ordem da chave.
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

                    #Validação do comando dito.
                    try:
                        metodo = dados['validacao']
                        valido = metodo(texto)
                    except:
                        print('Erro no método de validação')
                        break
            #Validação dos dados para sair da tela.
            if valido:
                lerBanco(sqlscript)
                confirmado_valido = False
                while confirmado_valido is not True:
                    print('Deseja gerar outro gráfico? SIM ou NÃO?')
                    speechConfirma()
                    texto = recognizer.recognizer()
                    if texto.lower() == 'não' or texto.lower() == 'sim':
                        confirmado_valido = True
                        if texto.lower() == 'não':
                            valido = True
                            confirmado = True
                            janela.after(3000, lambda: janela.destroy())
                        else:
                            entTempoGrafico['text'] = "Qual o tempo desejado do gráfico?"
                            entTempoGrafico['bg'] = "white"
                            if os.path.isfile('grafico.png'):
                                os.remove('grafico.png')
        print('Saiu')


def grafico_pet():
    # Thread para rodar duas ações ao mesmo tempo.
    t = threading.Thread(target=speech)
    t.start()
    t = threading.Thread(name='my_service', target=valida)
    t.start()

    # ------------------------------ TKINTER INTERFACE ------------------------------ #
    global janela
    janela = Toplevel()
    janela.geometry("650x650+300+100")
    janela.wm_title("Assistente Pet")
    lbltitulo = Label(janela, text="GRÁFICOS DO PET", font=("Arial", 10, "bold")).place(x=200, y=10)

    # ===== VARIAVEIS LOCAIS ===== #
    # global janela
    global entTempoGrafico
    entTempoGrafico = StringVar()
    global imagemGrafico

    # Labels de idenficação dos campos
    Label(janela, text="Tempo do gráfico:", font=("Arial", 10, "bold")).place(x=30, y=50)
    Label(janela, text="Informe uma opção: Semanal/ Mensal/ Ano", font=("Arial", 8, "bold", "italic")).place(x=30, y=80)
    # Labels que aparecerão as respostas para nome e tipo do pet
    entTempoGrafico = Label(janela, font=("Arial", 10), bg='white', width='75', height='2', text='Qual o tempo do gráfico?')
    entTempoGrafico.place(x=30, y=110)

    janela.mainloop()
