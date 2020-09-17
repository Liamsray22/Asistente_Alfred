import Interprete as inter
import speech_recognition as sr
import random as rn
import Hablar as sp
from pocketsphinx import LiveSpeech
import os


bot = sp.Hablar()
index = 0
while True:
    print('Espere....')
    bot.iniciarALFRED(index)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando....")
        # help(r)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # Si se entendió el audio
        comando = r.recognize_google(audio, language='es-MX')
        print('>>>',comando)
        inter.interpretar(str(comando).lower())  # lo que se debe hacer con el comando de audio
        index = rn.randint(1,4)

    except sr.UnknownValueError:
        # si no se entendió
        print("No te pude entender")
    except sr.RequestError as e:
        # si no se tiene conexión a internet o al servicio de google
        print("No pude obtener respuesta del servicio de Google Speech Recognition; {0}".format(e))
        break
