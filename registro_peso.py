'''                                           Registro de Peso                                                          '''
from tkinter import *
import recognizer

#def registro_peso():
'''Validação dos dados----------------------------------------------------------------------------------------------'''
'''
    #Função secundária que chama função primária.
    def valida(entrada):
        valid = False
        while valid is not True:
            if not entrada == '' or not entrada == None:
                valida_num(entrada)
                valid = True
                print('ok')
            else:
                # messenger["text"] = 'Não ouvi, repita novamente'
                print('Não ouvi, repita novamente')
                entrada = recognizer.recognizer()
'''

def valida_num(value):
    n = None
    val = False
    while val is not True:
        try:
            entrada_d = value.split(' ')
            numero = entrada_d[0]
            print(f'O Número informado foi {numero}')
            numero = numero.replace(',', '.')
            n = float(numero)
            audio_peso.set(n)
            print(n)
            val = True
            return True
        except AttributeError:
            print('Valor inválido, repita')
            val = False
            break
        except ValueError:
            print('Valor não foi dito corretamente.')
            val = False
            break
        except:
            print('Valor inválido')
            val = False
            break

def valida():
    confirmado = False
    while confirmado is not True:
        campos = {'Peso do pet': {'validacao': valida_num, 'mensagem': 'Qual o peso do Pet hoje'}}

        valido = False
        while valido is not True:
            for campo in campos.keys():
                dados = campos[campo]
                #messenger["text"] = dados['mensagem']
                print(dados['mensagem'])
                texto = recognizer.recognizer()

                try:
                    metodo = dados['validacao']
                    valido = metodo(texto)
                except:
                    #messenger["text"] = 'Erro no método de validação'
                    print('Erro no método de validação')
                    break

            if valido:
                #messenger["text"] = 'Deseja confirmar sim ou não'
                print('Deseja confirmar sim ou não')
                texto = recognizer.recognizer()
                if texto.title() == 'Sim':
                    valido = True
                    confirmado = True

'''Interface gráfica------------------------------------------------------------------------------------------------'''

janela = Tk()

audio_peso = StringVar()
audio_peso.set("")

reg_peso = Label(janela, bg='white', width='50', textvariable=audio_peso)
reg_peso.place(x=40, y=130)

# Textos de cada campo.
tex_pes = Label(janela, text="Peso:")
tex_pes.place(x=40, y=105)

# Mensagens de erro ou informativa para o usuário.
lb_peso = Label(janela, text='')
lb_peso.place(x=170, y=155)

messenger = Label(janela, text='')
messenger.place(x=35, y=280)

petbt = Button(janela, text='Valida', command=valida)
petbt.place(x=10, y=300)

janela.title("Registro Peso")
janela.geometry("500x500+300+300")
janela.mainloop()

#registro_peso()

