import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
        print("Diga algo:")
        audio = recon.listen(source)
print()
print()
print("O texto reconhecido é:")
print()
print()
print(recon.recognize_google(audio, language='pt'))
print()
print()
x = input("Digite uma tecla para finalizar")



