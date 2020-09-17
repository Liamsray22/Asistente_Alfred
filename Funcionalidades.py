import subprocess as sub
import pyautogui as auto
from time import sleep
import webbrowser as wb
import sys
import Hablar as sp
import Escuchar as ls
import random as rn

bot = sp.Hablar()
oido = ls.Escuchar()

# Funcionalidad: Abrir Bloc de Notas
def abrirNotas():
    # sleep(1.5)
    bot.Dice('Abriendo Bloc de Notas')
    sub.call('start notepad.exe', shell=True)

def llamarAlfred():
    bot.Dice('estoy aquí señor')

# Funcionalidad: Abrir YouTube
def abrirYoutube(param):
    if 'de' in param:
        indice = param.find('de')
        parame = str(param)[indice+7:len(param)]
        bot.Dice('Abriendo YouTube, buscando {}'.format(parame))
        wb.open_new_tab('https://www.youtube.com/results?search_query={}'.format(parame))
    else:
        bot.Dice('Abriendo YouTube')
        wb.open_new_tab('https://www.youtube.com')

    return None

#Funcionalidad: Presionar dos teclas a la vez
def funcionesHotkey(pri,seg):
    auto.hotkey(pri,seg)

#Funcionalidad: Presionar una tecla
def funcionesPress(uni):
    auto.press(uni)

# Funcionalidad: Abrir ITLA Virtual
def abrirVirtual():
    bot.Dice('Abriendo Itla Virtual')
    wb.open_new_tab('https://plataformavirtual.itla.edu.do/my/')
    return None


# Funcionalidad: Buscar en Google
def busqueda():
    search = oido.listen('Que le Busco, señor?')
    if search == 'nada':
        bot.iniciarALFRED(0)
        return None
    contextoBusqueda(search)


# Contexto: Busqueda
def contextoBusqueda(param):
    wb.open_new_tab('https://www.google.com/search?q={}'.format(param))


# Funcionalidad: Busqueda Automatica
def busquedaA(param):
    indice = 0
    parame = param.split(' ')
    if 'busca' in parame:
        indice = parame.index('busca')
        parame.pop(indice)
    elif 'buscame' in parame:
        indice = parame.index('buscame')
        parame.pop(indice)
    elif 'búscame' in parame:
        indice = parame.index('búscame')
        parame.pop(indice)
    elif 'buscar' in parame:
        indice = parame.index('buscar')
        parame.pop(indice)
    else:
        bot.Dice('Hay Panicooo, Hay Panicoooo')

    parame = ' '.join(parame)
    bot.Dice('Abriendo Google, buscando {}'.format(parame))
    wb.open_new_tab('https://www.google.com/search?q={}'.format(parame))


# Funcionalidad: Cerrar Ventana de Google
def cerrarVentana(param):
    param = param.split(' ')
    if 'dos' in param:
        auto.hotkey('ctrl', 'w')
        sleep(1.5)
        auto.hotkey('ctrl', 'w')
        bot.Dice('Dos Ventanas Cerradas')

    else:
        auto.hotkey('ctrl', 'w')
        bot.Dice('Ventana Cerrada')

# Funcionalidad: Abrir Ventana de Google
def abrirVentana(param):
    param = param.split(' ')
    if 'dos' in param:
        auto.hotkey('ctrl', 't')
        sleep(1.5)
        auto.hotkey('ctrl', 't')
        bot.Dice('Dos Ventanas Abiertas')

    else:
        auto.hotkey('ctrl', 't')
        bot.Dice('Ventana Abierta')



# Funcionalidad: Escribir
def escribir(param):
    parame = param.split(' ')
    if 'escribe' in parame:
        indice = parame.index('escribe')
        parame.pop(indice)
    elif 'escribeme' in parame:
        indice = parame.index('escribeme')
        parame.pop(indice)
    else:
        bot.Dice('Hay Panico, Hay Panico')

    parame = ' '.join(parame)
    bot.Dice(parame)
    auto.write(parame)

#Funcionalidad: Poner Musica
def escucharMusica():
    genero = oido.listen('Algun genero en específico?')
    if genero == 'no' or genero == 'No' or genero == 'que no' or genero == 'qué no':
        wb.open_new_tab('https://www.youtube.com/watch?v=c8i-NAi8CJU&list=RDMMc8i-NAi8CJU&start_radio=1')
        return None
    contextoEscucharMusica(genero)
#Contexto: Escuchar Musica
def contextoEscucharMusica(genero):
    if genero == 'lofi' or genero == 'Luffy':
        wb.open_new_tab('https://www.youtube.com/watch?v=5qap5aO4i9A')
    elif genero == 'indi' or genero == 'indie':
        wb.open_new_tab('https://www.youtube.com/watch?v=2chfsFTNEXw&t')
    elif genero == 'jazz':
        wb.open_new_tab('https://www.youtube.com/watch?v=neV3EPgvZ3g')
    elif genero == 'openins' or genero == 'opening':
        wb.open_new_tab('https://www.youtube.com/watch?v=pmanD_s7G3U&list=RDQME_sLoyaiKQw&start_radio=1')
    else:
        print(genero)
        wb.open_new_tab('https://www.youtube.com/watch?v=sgOoSTcuLio')

#Funcionalidad: Ver Pagina de Peliculas
def verPelicula():
    wb.open_new_tab('https://pelisplushd.net/')

#Funcionalidad: Ver Pagina de Anime

def verAnime():
    wb.open_new_tab('https://animeflash.xyz/')



#Funcionalidad: Cerrar
def terminarALFRED():
    index = rn.randint(1, 4)
    frasesDespedidas=['Me retiro señor', 'Llameme si me necesita','Hasta luego','No dude en llamarme mas tarde','Quedo a la orden',
                      'Hasta la proxima','Cualquier cosa sabe donde encontrarme']
    bot.Dice(frasesDespedidas[index])
    sys.exit()