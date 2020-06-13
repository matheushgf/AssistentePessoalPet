import speech_recognition
command_lists = ['registro de peso','registro de ração','registro de animal']

def recognizer():
        speech_recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
                print("Ouvindo")
                audio = speech_recognizer.listen(source)
        print("O texto reconhecido é:")
        print(speech_recognizer.recognize_google(audio, language='pt'))

        return speech_recognizer.recognize_google(audio, language='pt')

def command_verification(user_command):
        flag=False
        for item in command_lists:
                if user_command == item:
                        flag=True
        return flag





