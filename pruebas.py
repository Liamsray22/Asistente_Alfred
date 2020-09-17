# import subprocess as sub
# import time
# import pyautogui as auto
# from time import sleep
#
# # auto.hotkey('win','d')
# sleep(1)
# auto.moveTo(500, 410)
# auto.click()
# auto.write('20186308')
# # auto.doubleClick()
# # sub.Popen('C:/Program Files (x86)/VictorVal/Fallout 3 Gold Repack/', shell=True)
#


import pyttsx3 as speak
import pyautogui as gui
import time

print('hola')
alfred = speak.init()
# help(alfred)
acentos = alfred.getProperty('voices')
print(acentos)

for a in acentos:
    print(a.id)

alfred.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
alfred.setProperty('rate',130)


alfred.say('Vamos Mesi eres el mejor de toditita españa')
alfred.runAndWait()


