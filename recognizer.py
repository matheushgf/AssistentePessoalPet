import speech_recognition

command_lists = {'registro de peso':{},'registro de ração':{},'registro de animal':{'nome_funcao':'registro_pet', 'nome_arquivo':'registro_pet'}}

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
                module = __import__(dados["nome_arquivo"])
                metodo = getattr(module, dados[dados["nome_funcao"]])
                metodo()






