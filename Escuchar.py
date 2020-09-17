import speech_recognition as sr
import Hablar as sp


bot = sp.Hablar()

class Escuchar:

        def listen(self,mensaje):
            bot.Dice(mensaje)
            r = sr.Recognizer()
            with sr.Microphone(device_index=0, sample_rate=None, chunk_size=1024) as source:
                print(mensaje)
                # help(r)
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                comando = r.recognize_google(audio, language='es-MX')
                return comando
            except sr.UnknownValueError:
                print("Repetir")
            except sr.RequestError as e:
                print("Error de Google; {0}".format(e))