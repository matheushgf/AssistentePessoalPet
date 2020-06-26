audio_peso = '54,09 kg'  #Vai avaliar o comando recebido.

value = audio_peso.split(' ')

#for val in value:
#    if val.isdigit() == True:


try:
    numero = value[0]
except SyntaxError:
    numero = partes[0].replace(',', '.')
except (SyntaxError, NameError, TypeError):
    print('Invalido, diga novamente.')

'----------------------------------------------------------------------------------'
while True:

    def verification(user_func):
        if user_func in command_lis.keys():

            try:
                return lb_peso["text"] = ''
            except:
                return message["text"]'Não entendi, repita por favor'
        else:
            return 'Comando não encontrado'