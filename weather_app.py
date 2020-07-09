import requests
import json
from datetime import date
import datetime
from tkinter import *
from recognizer import *
import speech_recognition
import pyttsx3

accuweatherAPIKey = 'eKzK8IAPh3cqE26tBucNy2oDRNvwJugM'
dias_semana = ["Domingo","Segunda-feira","Terça-feira","Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"];

def pegarCoordenadas():
    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code != 200):
        print('Não foi possível obter a localização.')
        return None
    else:
        try:
            localizacao = json.loads(r.text)
            coordenadas = {}
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            return coordenadas
        except:
            return None
    
def pegarCodigoLocal(lat,long):
    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
    + "search?apikey=" +  accuweatherAPIKey \
    + "&q=" + lat + "%2C"+ long +"&language=pt-br"

    r = requests.get(LocationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o código do local.')
        return None
    else:
        try:
            locationResponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ", " \
                        + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
                        + locationResponse['Country']['LocalizedName']
            infoLocal['codigoLocal'] = locationResponse['Key']
            return infoLocal
        except:
            return None

def pegarTempoAgora(codigoLocal, nomeLocal):

    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                              + codigoLocal + "?apikey=" + accuweatherAPIKey \
                              + "&language=pt-br"
    r = requests.get(CurrentConditionsAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o clima atual.')
        return None
    else:
        try:
            CurrentConditionsResponse = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = CurrentConditionsResponse[0]['WeatherText']
            infoClima['temperatura'] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None

def pegarPrevisao5Dias(codigoLocal):
    DailyAPIUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
                              + codigoLocal + "?apikey=" + accuweatherAPIKey \
                              + "&metric=true&language=pt-br&details=true&getphotos=false"
    r = requests.get(DailyAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a previsão para os próximos dias.')
        return None
    else:
        try:
            DailyResponse = json.loads(r.text)
            infoClima5Dias = []
            for dia in DailyResponse['DailyForecasts']:
                climaDia = {}
                climaDia['max'] = dia['Temperature']['Maximum']['Value']
                climaDia['min'] = dia['Temperature']['Minimum']['Value']
                climaDia['clima'] = dia['Day']['IconPhrase']
                diaSemana = date.fromtimestamp(dia['EpochDate']).strftime("%w")
                climaDia['dia'] = dias_semana[int(diaSemana)]
                infoClima5Dias.append(climaDia)
            return infoClima5Dias
        except:
            return None
        
def pegarPrevisao12Horas(codigoLocal):
    HoursAPIUrl = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" \
    + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br&details=false&metric=true"
    r = requests.get(HoursAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a previsão para os próximos dias.')
        return None
    else:
        try:
            HoursAPIResponse = json.loads(r.text)
            infoClimaHours = []
            for hora in HoursAPIResponse:
                horaDia = {}
                horaDia['hora'] = datetime.datetime.fromtimestamp(hora['EpochDateTime']).strftime('%d-%m-%Y %H:%M')
                horaDia['temp'] = hora['Temperature']['Value']
                horaDia['clima'] = hora['IconPhrase']
                horaDia['chuva'] = hora['HasPrecipitation']
                horaDia['probChuva'] = hora["PrecipitationProbability"]
                infoClimaHours.append(horaDia)
            return infoClimaHours
        except:
            return None

def melhorHora(previsao):
    melhoresHoras = []
    for hora in previsao:
        if (int(hora['hora'][10:13]) <= 23) and (int(hora['hora'][10:13]) >= 6):
            melhoresHoras.append(hora)
    horas = []
    menorprob = 100
    for hora in melhoresHoras:
        if hora['probChuva'] <= menorprob:
            menorprob = hora['probChuva']
    for hora in melhoresHoras:
        if hora['probChuva'] == menorprob:
            horas.append(hora)
    media = 0
    for hora in horas:
       media += hora['temp']
    media = media / len(horas)
    diferencaEscolha = 100
    diferenca = 100
    horaIdeal = {}
    for i in melhoresHoras:
        diferenca = media - i['temp']
        if diferenca < 0:
            diferenca = diferenca * -1
        if diferenca < diferencaEscolha:
            diferencaEscolha = diferenca
            horaIdeal = i
    if horaIdeal['chuva'] == True:
        return {"Mensagem": "Não há melhor hora pra sair nas proximas 12 horas"}

    return {"horaIdeal":horaIdeal['hora'],"temperatura":horaIdeal['temp']}

def weather_app():
    coordenadas = pegarCoordenadas()
    codigoLocal = pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])
    pegarPrevisao = pegarPrevisao12Horas(str(codigoLocal['codigoLocal']))
    pegarMelhorHora = melhorHora(pegarPrevisao)
    horaIdealEscolhida = f"O melhor horário para passear com o seu animal é {pegarMelhorHora['horaIdeal']}."
    print(horaIdealEscolhida)
    tempIdealEscolhida = f"A previsão de temperatura neste momento será de {pegarMelhorHora['temperatura']} graus."
    print(tempIdealEscolhida)

    # INICIALIZANDO O OBJETO GRAFICO DA TELA

    root = Tk()

    textoFalado = f"{horaIdealEscolhida} e {tempIdealEscolhida}"
    def speech():
        label2audio = (textoFalado)
        en = pyttsx3.init()
        en.say(label2audio)
        en.runAndWait()

    # PASSANDO AS MEDIDAS E CONFIGURAÇÃO DA TELA
    root.geometry("400x320+0+0")
    root.title("Assistente de Clima")
    root.configure(background='#707070')

    # CONFIGURANDO O TEMPORIZADOR DE FECHAMENTO DA TELA
    root.after(15000,lambda:root.destroy())

    lblTitulo = Label(root, font=('arial', 9), text=horaIdealEscolhida, width='55').place(x=5, y=90, height=50)

    lblTitulo2 = Label(root, font=('arial', 9), text=tempIdealEscolhida, width='55').place(x=5, y=160, height=50)

    t = threading.Thread(target=speech)
    t.start()
    root.mainloop()



#weather_app()

        





    
