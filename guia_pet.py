from tkinter import *
import threading
import tkinter.messagebox as MessageBox
from datetime import date
import datetime
import recognizer
import crud
import pymysql as mysql
import time
import pyttsx3


# ======================= FUNCOES DO SISTEMA ======================== #
def speech():
    label2audio = ("Diga qual o PET você deseja ter dicas:")
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def speechDicas(textoFalado):
    label2audio = (textoFalado)
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def validaCategoria(entrada):

    global valorTipoPet

    try:

        if entrada == '':
            entTipoPet['text'] = 'Insira o tipo de pet!'
            entTipoPet['bg'] = '#FF6347'
            return False
        tipoPet = entrada
        entTipoPet['text'] = tipoPet.title()
        entTipoPet['bg'] = '#90EE90'
        valorTipoPet = tipoPet.title()
        return True
    except AttributeError:
        entTipoPet['text'] = 'Valor inválido, repita'
        entTipoPet['bg'] = '#FF6347'
    except ValueError:
        entTipoPet['text'] = 'Valor não foi dito corretamente.'
        entTipoPet['bg'] = '#FF6347'
    except:
        entTipoPet['text'] = 'Valor inválido'
        entTipoPet['bg'] = '#FF6347'

def pegaCategoria():
    tipoPet = valorTipoPet

    if tipoPet.lower() == 'cachorro':

        dicas = ['Dois cães podem ser o dobro da diversão,\nmas é importante que cada um tenha uma\nrelação individual com você e a capacidade\nde ficar sozinho às vezes.',
                 'Tosse de canil é causada por vírus e bactérias.\nA tosse pode persistir por até 6 semanas.\nO tratamento pode ser necessário ou não,\ndependendo da gravidade.',
                 'Use uma dieta apropriada para a idade. Filhotes\nprecisam de proteínas e calorias\n extras encontradas em fórmulas de crescimento.\nCães mais velhos precisam de menos, a fim de\nmanter sua figura jovem.',
                 'A maioria das ações que os donos definem como mau\ncomportamento são, na verdade, comportamentos\nnormais feitos na hora errada e no\nlugar errado. Entenda mais sobre a psicologia canina.',
                 'Os cães adolescentes testam limites e parecem possuir\nenergia ilimitada – não muito diferente de\nseus colegas humanos. Exercícios aeróbicos,\nmuitas brincadeiras com desafios mentais\ne um manejamento cuidadoso irão ajudar vocês dois a\natravessar esse estágio difícil do desenvolvimento.']

    elif tipoPet.lower() == 'gato':

        dicas = ['Compre ração de boa qualidade e sirva de forma\ngradativa durante o dia. Patês com sabor especial\npodem ser servidos periodicamente para o\nanimal como uma forma de agradá-lo.\nAlém disso, o leite é a sobremesa dos gatos, eles adoram e\nnão vivem sem.',
                 'A água é tão importante para os gatos como é para\nos seres humanos. Sempre sirva para o seu animal\nde estimação água filtrada e troque o conteúdo\nda vasilha por pelo menos duas vezes ao dia,\no ideal é trocar 3 vezes. Dessa forma a água estará\nsempre fresquinha. ',
                 'Sempre arranje um tempinho para brincar com o seu gato.\nIsso o estimula a ter uma vida mais tranquila.\nVocê pode produzir os brinquedos na sua própria casa,\ngastar muito pouco e garantir a diversão. ',
                 'Gato ama conforto e proporcionar isso para\nele na hora do sono é uma prova de amizade.\nA cama pode ser comprada em algum Pet shop ou de papelão,\nfeita em casa mesmo. O importante é que ela seja acolchoada\ne tenha um cobertor para animais. ',
                 'Os gatos aprendem a fazer as necessidades fisiológicas\nna caixa de areia por conta própria. Manter a caixa sempre\nlimpa e cheia de areia é essencial, caso contrário ele\ncomeçará a urinar em outros lugares e a limpeza será mais\ncomplicada. '
                 ]

    elif tipoPet.lower() == 'outros':

        dicas = ['Dica de Outros 1',
                 'Dica de Outros 2',
                 'Dica de Outros 3',
                 'Dica de Outros 4',
                 'Dica de Outros 5']

    else:

        entTipoPet['text'] = 'Insira o tipo do Pet corretamente!'
        entTipoPet['bg'] = '#FF6347'
        return False

    for dica in dicas:

        entDicas['text'] = dica
        speechDicas(dica)
        time.sleep(2)

    return True

def valida():
    #    return True
    confirmado = False
    while confirmado is not True:
        # Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
        campos = {
            'categoria': {'validacao': validaCategoria, 'mensagem': 'Dicas de qual tipo de pet? Cachorro/Gato/Outros'}
        }
        #       Laço para percorrer todos os campos pela ordem da chave.
        confirmado = False
        while confirmado is not True:
            for campo in campos.keys():
                valido = False
                while valido is not True:
                    # Seleção do campo.
                    dados = campos[campo]
                    texto = recognizer.recognizer()

                    #               Validação do comando dito.
                    try:
                        metodo = dados['validacao']
                        valido = metodo(texto)
                    except:
                        break

            if valido:

                if pegaCategoria():

                    janela.after(5000, lambda: janela.destroy())



t = threading.Thread(name='my_service', target=valida)
t.start()


# ========================== JANELA TKINTER ========================== #
janela = Tk()
janela.geometry("350x500+500+200")
janela.wm_title("Assistente Pet")
lblTitulo = Label(janela, text="GUIA PET", font=("Arial", 10, "bold")).place(x=70, y=10)

# ===================== VARIAVEIS LOCAIS E GLOBAIS ===================== #
global entTipoPet
entTipoPet = StringVar()

# Labels de idenficação dos campos
lblTipoPet = Label(janela, text="Diga o tipo de pet que quer dicas:", font=("Arial", 10, "bold")).place(x=10, y=50)

# Labels que aparecerão as respostas para nome e tipo do pet
#entTipoPet = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', textvariable=txtMarcaRacao)
entTipoPet = Label(janela, font=("Arial", 10), bg='white', width='40', height='2', text="Qual a Categoria das dicas?")
entTipoPet.place(x=10, y=80)

entDicas = Label(janela, font=("Arial", 10), bg='white', width='40', height='20', text="")
entDicas.place(x=10, y=160)

t = threading.Thread(target=speech)
t.start()

janela.mainloop()
