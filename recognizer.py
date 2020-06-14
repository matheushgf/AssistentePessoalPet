import speech_recognition
import importlib

command_lists = {'registro de peso':{'nome_funcao':'registro_peso', 'nome_arquivo':'registro_peso'},'registro de animal':{'nome_funcao':'registro_pet', 'nome_arquivo':'registro_pet'}}

def recognizer():
        speech_recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
                print("Ouvindo")
                audio = speech_recognizer.listen(source)
        print("O texto reconhecido é:")
        print(speech_recognizer.recognize_google(audio, language='pt'))

        return speech_recognizer.recognize_google(audio, language='pt')

def command_verification(user_command):

        if ( user_command in command_lists.keys()):
                dados = command_lists[user_command]
                module = importlib.import_module(dados['nome_arquivo'])
                metodo = getattr(module, dados['nome_funcao'])

                try:
                        metodo()
                        return 'Comando executado'
                except:
                        return 'Erro ao executar método'
        else:
                return 'Comando não encontrado'






