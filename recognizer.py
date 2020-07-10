import speech_recognition
import importlib
import pyttsx3
import threading
import pyttsx3

command_lists = {'registro de ração':{'nome_funcao':'registro_racao','nome_arquivo':'registro_racao'},
                 'registro de lembrete':{'nome_funcao':'lembrete_pet', 'nome_arquivo':'lembrete_pet'},
                 'clima':{'nome_funcao':'weather_app', 'nome_arquivo':'weather_app'},
                 'registro de peso':{'nome_funcao':'registro_peso', 'nome_arquivo':'registro_peso'},
                 'registro de animal':{'nome_funcao':'registro_pet', 'nome_arquivo':'registro_pet'},
                 'dicas de filme':{'nome_funcao':'dicasDeFilme', 'nome_arquivo':'api6sem'}
                 }

def speech():
    label2audio = ('Comando não encontrado')
    en = pyttsx3.init()
    en.say(label2audio)
    en.runAndWait()

def recognizer():
        try:
                speech_recognizer = speech_recognition.Recognizer()

                with speech_recognition.Microphone() as source:
                        print("Ouvindo")
                        audio = speech_recognizer.listen(source)

                saida = speech_recognizer.recognize_google(audio, language='pt')
                saida = saida.strip()
                print("O texto reconhecido é:")
                print(saida)

                return saida
        except:
                return ""

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
                t = threading.Thread(target=speech)
                t.start()
                return 'Comando não encontrado'