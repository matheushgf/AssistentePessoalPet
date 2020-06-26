'''                                           Registro de Ração                                                         '''

from tkinter import *
from recognizer import recognizer
#from AssistentePessoalPet import crud
#import datetime

def registro_peso():
    '''Interface gráfica------------------------------------------------------------------------------------------------'''

    janela = Tk()

    audio_racao = StringVar()
    audio_racao.set("")

    reg_peso = Label(janela, bg='white', width='50', textvariable=audio_racao)
    reg_peso.place(x=40, y=130)

    # Textos de cada campo.
    tex_pes = Label(janela, text="Ração:")
    tex_pes.place(x=40, y=105)

    # Mensagens de erro ou informativa para o usuário.
    lb_peso = Label(janela, text='')
    lb_peso.place(x=170, y=155)

    messenger = Label(janela, text='')
    messenger.place(x=35, y=280)

    janela.title("Registro Ração")
    janela.geometry("500x500+300+300")
    janela.mainloop()

    '''Validação dos dados----------------------------------------------------------------------------------------------'''

    #Função secundária que chama função primária.
    def valida(entrada):

        if entrada == '' or entrada == None:
            valid = False
            while valid is not True:
                messenger["text"] = 'Não ouvi, repita novamente'
                entrada = recognizer()
                if entrada != '' or entrada != None:
                    valida_num(entrada)
                    valid = True
                    return  True
        else:
            valida_num(entrada)
            return True

    #Função primária
    def valida_num(value):
        n = None

        try:
            entrada_d = value.split(' ')
            numero = entrada_d[0]
            messenger["text"] = f'O valor informado foi {numero}'
            numero = numero.replace(',', '.')
            audio_racao.set(str(numero))
        except AttributeError:
            lb_peso["text"] = 'Valor inválido, repita'
        except ValueError:
            lb_peso["text"] = 'Valor não foi dito corretamente.'
        except:
            lb_peso["text"] = 'Valor inválido'

    #Comandos feitos por voz, com chamada dinâmica para a Lebal
    confirmado = False
    while confirmado is not True:

        campos = {
            'Ração pet': {'validacao': valida, 'mensagem': 'Qual é o peso da ração'}
        }

        for campo in campos.keys():
            valido = False
            while valido is not True:
                dados = campos[campo]
                messenger[""] = dados['mensagem']
                texto = recognizer()

                try:
                    metodo = dados['validacao']
                    valido = metodo(texto)
                except:
                    messenger["text"] = 'Erro no método de validação'
                    break

        if valido:
            messenger["text"] = 'Deseja confirmar sim ou não'
            texto = recognizer()

            if texto == 'Sim':
                valido = True
                confirmado = True

registro_peso()

print('Saiu')