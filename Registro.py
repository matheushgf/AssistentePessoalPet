'''                                           Registro de Peso e Ração                                                  '''

from tkinter import *
import speech_recognition

def registro_peso_racao():
    registro_peso = []  #Salvar no banco.
    registro_racao = []  #Salvar no banco.
    reg_rac_min = 0
    valid = ''
    valid2 = ''
    
    
    '''Validação dos dados----------------------------------------------------------------------------------------------'''
    
    # Funcao responsavel por ouvir e reconhecer a fala
    def rec():
        global valid
        speech_recognizer = speech_recognition.Recognizer()
    
        with speech_recognition.Microphone() as source:
            audio_final_peso = speech_recognizer.listen(source)
        try:
            audio_peso.set(speech_recognizer.recognize_google(audio_final_peso, language='pt'))
            valid = speech_recognizer.recognize_google(audio_final_peso, language='pt')
            rac["text"] = ""
    
        except:
            rac["text"] = "Não entendi, repita por favor."
    
    def rec1():
        global valid2
        speech_recognizer = speech_recognition.Recognizer()
    
        with speech_recognition.Microphone() as source:
            audio_final_rac = speech_recognizer.listen(source)
        try:
            audio_rac.set(speech_recognizer.recognize_google(audio_final_rac, language='pt'))
            valid2 = speech_recognizer.recognize_google(audio_final_rac, language='pt')
            rac["text"] = ""
    
        except:
            rac["text"] = "Não entendi, repita por favor."
    
    def clear():
        audio_peso.set("Diga o peso")
        audio_rac.set('Diga a quantidade de ração')
    
    def validad():
    
        global reg_rac_min
    
        if valid.isalpha() == True and valid2.isalpha() == True:
    
            lb_peso["text"] = 'Dado inválido, digite apenas números entre (0-9).'
            lb_racao["text"] = 'Dado inválido, digite apenas números entre (0-9).'
    
        elif valid.isalpha() == True and valid2.isalpha() == False:
    
            lb_peso["text"] = 'Dado inválido, digite apenas números entre (0-9).'
            lb_racao["text"] = ''
    
        elif valid.isalpha() == False and valid2.isalpha() == True:
    
            lb_peso["text"] = ''
            lb_racao["text"] = 'Dado inválido, digite apenas números entre (0-9).'
    
        elif not valid.isnumeric() and len(valid) == 0 and str(valid) == '':
    
            lb_peso["text"] = 'Dado inválido, digite novamente.'
    
        else:
    
            lb_peso["text"] = ''
            lb_racao["text"] = ''
    
            reg_rac_min = float(valid) * 0.03
    
            if not valid2.isnumeric() and len(valid2) == 0 and str(valid2) == '':
    
                lb_racao["text"] = 'Dado inválido, digite novamente.'
    
            elif float(valid2) <= reg_rac_min:  # Condição de invalidez por minimo.
    
                rac["text"] = 'A quantidade de ração não pode ser menos que o mínimo indicado!'
    
            else:
    
                rac["text"] = ''
                lb_peso["text"] = ''
                lb_racao["text"] = ''
                save["text"] = 'Dados salvos com sucesso.'
    
                str(valid2)
                registro_racao.append(valid2)
    
                str(valid)
                registro_peso.append(valid)
    
    '''Interface gráfica------------------------------------------------------------------------------------------------'''
    
    janela = Tk()
    
    audio_peso = StringVar()
    audio_rac = StringVar()
    audio_peso.set("Diga o peso")
    audio_rac.set('Diga a quantidade de ração')
    
    reg_peso = Label(janela, bg='white', width='50', textvariable=audio_peso)
    reg_peso.place(x=40, y=130)
    
    
    reg_rac = Label(janela, bg='white', width='50', textvariable=audio_rac)
    reg_rac.place(x=40, y=220)
    
    #Textos de cada campo.
    tex_pes = Label(janela, text="Peso:")
    tex_pes.place(x=40, y=105)
    
    tex_reg = Label(janela, text="Ração:")
    tex_reg.place(x=40, y=195)
    
    #Mensagens de erro ou informativa para o usuário.
    lb_peso = Label(janela, text='')
    lb_peso.place(x=170, y=155)
    
    lb_racao = Label(janela, text='')
    lb_racao.place(x=170, y=245)
    
    save = Label(janela, text= '')
    save.place(x=155, y=340)
    
    rac = Label(janela, text='')
    rac.place(x=35, y=280)
    
    #Botão de salvamento
    bt = Button(janela, bg='green', width=15, text="OK", command=validad)
    bt.place(x=100, y=370)
    
    clear_bt = Button(janela, bg='red', text='Limpar campos', width=15, command=clear)
    clear_bt.place(x=260, y=370)
    
    peso_bt = Button(janela, text='Diga o peso', width=30, command=rec)
    peso_bt.place(x=120, y=420)
    
    racao_bt = Button(janela, text='Diga a quantidade', width=30, command=rec1)
    racao_bt.place(x=120, y=460)
    
    
    janela.title("Registro")
    janela.geometry("500x500+300+300")
    janela.mainloop()
    
    print(registro_peso, registro_racao)  #Resultado da execução do teste.
