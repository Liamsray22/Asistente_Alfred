import pyttsx3 as voz


class Hablar:

    def __init__(self):
        self.alfred = voz.init()
        self.alfred.setProperty('rate',150)
        self.alfred.setProperty('voice', 'TTS_MS_ES-MX_SABINA_11.0')  # voz con acento mexicano

    def iniciarALFRED(self,index):
        frasesQueMas = ['Que necesita señor?','Algo Mas señor?','Necesita algo mas señor?',
                  'En que mas puedo servirle señor?','De que otra forma puedo ayudarle señor?',
                  'Puedo hacer algo mas por usted señor?','Que mas necesita señor?','Otra cosa señor?',
                        'Hay Algo Mas señor?']

        self.alfred.say(frasesQueMas[index])
        self.alfred.runAndWait()
        self.alfred.stop()


    def Dice(self,texto):
        self.alfred.say(texto)
        self.alfred.runAndWait()
        self.alfred.stop()




