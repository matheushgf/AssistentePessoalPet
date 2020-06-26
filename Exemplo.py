''' Função por trás das operações de voz '''

from tkinter import *
from recognizer import recognizer

def valida(entrada):
    n = None

    #Parte do código usada no registro de peso (Pode ser adaptada e usada em outros).
    try:
        entrada_d = entrda.split(' ')
        numero = entrada_d[0]
        print(entrada_d)
        print(f'O Número informado foi {numero}')
        numero = numero.replace(',', '.')
        n = float(numero)
        return True
    except AttributeError:
        print('Valor inválido, repita')
    except ValueError:
        print('Valor não foi dito corretamente.')
    except:
        print('Valor inválido')

    print(n)
    print(type(n))

#Função para validar e sair da tela em questão.
def valida_nome_pet(texto):
    return True

confirmado = False
while confirmado is not True:

    #Caso seja necessário colocar mais campos no registro, deverá apenas seguir a forma a baixo, e colocar os dados e a função.
    campos = {
        'Nome do pet': {'validacao': valida_nome_pet, 'mensagem': 'Qual o nome do Pet ?'},
        'Idade do Pet': {'validacao': valida, 'mensagem': 'Qual a idade do Pet'}
    }

    #Laço para percorrer todos os campos pela ordem da chave.
    for campo in campos.keys():

        valido = False
        while valido is not True:

            #Seleção do campo.
            dados = campos[campo]
            print(dados['mensagem'])
            texto = recognizer()

            #Validação do comando dito.
            try:
                metodo = dados['validacao']
                valido = metodo(texto)
            except:
                print('Erro no método de validação')
                break

    #Validação dos dados para sair da tela.
    if valido:
        print('Deseja confirmar sim ou não')
        texto = recognizer()

        if texto == 'Sim':
            valido = True
            confirmado = True

print('Saiu')

'-----------------------------------------------------------------------------------------------------------------------'
'''
 def valida(entrada):
        n = None

        if entrada == '' or entrada == None:
            print('Não ouvi, repita novamente')
            continue
        else:
            try:
                entrada_d = entrda.split(' ')
                numero = entrada_d[0]
                print(entrada_d)
                print(f'O Número informado foi {numero}')

                numero = numero.replace(',', '.')

                n = float(numero)
                return True
            except AttributeError:
                print('Valor inválido, repita')
            except ValueError:
                print('Valor não foi dito corretamente.')
            except:
                print('Valor inválido')

            print(n)
            print(type(n))
    def valida_nome_pet(texto):
        return True
    confirmado = False
    while confirmado is not True:
        campos = {
            'Nome do pet': {'validacao': valida_nome_pet, 'mensagem': 'Qual o nome do Pet ?'},
            'Idade do Pet': {'validacao': valida, 'mensagem': 'Qual a idade do Pet'}
            }

        for campo in campos.keys():
            valido = False
            while valido is not True:
                dados = campos[campo]
                print(dados['mensagem'])
                texto = recognizer()

                try:
                    metodo = dados['validacao']
                    valido = metodo(texto)
                except:
                    print('Erro no método de validação')
                    break

        if valido:
            print('Deseja confirmar sim ou não')
            texto = recognizer()

            if texto == 'Sim':
                valido = True
                confirmado = True
registro_peso()

'''