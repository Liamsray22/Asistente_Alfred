
'''press(keys, presses=1, interval=0.0, logScreenshot=None, _pause=True)
        Performs a keyboard key press down, followed by a release.
        
        Args:
          key (str, list): The key to be pressed. The valid names are listed in
          KEYBOARD_KEYS. Can also be a list of such strings.
          presses (integer, optional): The number of press repetitions.
          1 by default, for just one press.
          interval (float, optional): How many seconds between each press.
          0.0 by default, for no pause between presses.
          pause (float, optional): How many seconds in the end of function process.
          None by default, for no pause in the end of function process.
        Returns:
          None'''


'''class Microphone(AudioSource)
     |  Microphone(device_index=None, sample_rate=None, chunk_size=1024)
     |  
     |  Creates a new ``Microphone`` instance, which represents a physical microphone on the computer. Subclass of ``AudioSource``.
     |  
     |  This will throw an ``AttributeError`` if you don't have PyAudio 0.2.11 or later installed.
     |  
     |  If ``device_index`` is unspecified or ``None``, the default microphone is used as the audio source. Otherwise, ``device_index`` should be the index of the device to use for audio input.
     |  
     |  A device index is an integer between 0 and ``pyaudio.get_device_count() - 1`` (assume we have used ``import pyaudio`` beforehand) inclusive. It represents an audio device such as a microphone or speaker. See the `PyAudio documentation <http://people.csail.mit.edu/hubert/pyaudio/docs/>`__ for more details.
     |  
     |  The microphone audio is recorded in chunks of ``chunk_size`` samples, at a rate of ``sample_rate`` samples per second (Hertz). If not specified, the value of ``sample_rate`` is determined automatically from the system's microphone settings.
     |  
     |  Higher ``sample_rate`` values result in better audio quality, but also more bandwidth (and therefore, slower recognition). Additionally, some CPUs, such as those in older Raspberry Pi models, can't keep up if this value is too high.
     |  
     |  Higher ``chunk_size`` values help avoid triggering on rapidly changing ambient noise, but also makes detection less sensitive. This value, generally, should be left at its default.
     |  '''

import Funcionalidades as fn

def sinonimar(comand, word):
    for i in word:
        encontrar = comand.find(i)
        if encontrar >= 0:
            return True
            break
    return False


#Interpretar
def interpretar(comando_de_audio):

    verVideo = sinonimar(comando_de_audio,['video','vídeo','entra a youtube','entra a yutub'])
    blocNota = sinonimar(comando_de_audio,['escribir','redactar','texto','bloc de notas','word'])
    terminar = sinonimar(comando_de_audio,['apagate','ya nada','apágate','retirate alfred','estare bien','adios','adiós','retírate'
        ,'retírate alfred','gracias','vete','callate','cállate', 'que te vayas'])
    itlaVirtual = sinonimar(comando_de_audio,['itla virtual', 'al virtual', 'el virtual'])
    buscarGoogle = sinonimar(comando_de_audio, ['abrir google', 'abre google', 'búscame en google',
                                                'búscame en google','google','guguel'])
    busquedaAuto = sinonimar(comando_de_audio,['busca','buscame','búscame', 'buscar'])
    cerrarVent = sinonimar(comando_de_audio,['cerrar ventana','cierra la ventana','cierra la pestaña','cerrar pestaña',
                                                'cierrame la ventana','cierrame la pestaña','cerrar dos ventanas', 'cierra dos ventanas',
                                             'cerrar dos pestañas','cierra dos pestañas'])
    abrirVent = sinonimar(comando_de_audio,['abrir ventana', 'abre la ventana', 'abre la pestaña', 'abrir pestaña',
                               'abreme la ventana', 'abreme la pestaña','abrir dos ventanas','abre dos ventanas',
                                             'abrir dos pestañas','abre dos pestañas'])
    escribe = sinonimar(comando_de_audio,['escribe','escribeme'])
    espacio = sinonimar(comando_de_audio,['espacio','pon espacio','pon un espacio'])
    musica = sinonimar(comando_de_audio,['escuchar música','oir música','pon música','reproduce música','pon la música',
                                         'oír música','escuchar musica','oir musica','pon musica','reproduce musica','pon la musica',
                                         'oír musica'])
    enter = sinonimar(comando_de_audio,['enter','dar enter','entrar','dale enter'])
    pausarResumir = sinonimar(comando_de_audio,['pausar','resumir','ponle pausa','resumela','resúmela','dale play',
                                                'dale plei','pausa','sigue'])
    sigMusica = sinonimar(comando_de_audio,['siguiente','la que sigue','cambiar cancion','cambiar canción'])
    antMusica = sinonimar(comando_de_audio,['anterior','retroceder cancion','dale pa atra','dale pa atras','dale pa atrás',
                                            'dale para atrás'])
    cambiarProg = sinonimar(comando_de_audio, ['cambiar programa','cambia programa','cambio de programa'])
    cambiarPest = sinonimar(comando_de_audio, ['cambiar pestaña','cambia pestaña','cambio de pestaña'])
    pelicula = sinonimar(comando_de_audio,['ver una pelicula', 'ver pelicula', 'una pelicula','ver películas','ver película',
                                           'una película'])
    anime = sinonimar(comando_de_audio,['ver anime','pon anime','un anime','veamos anime','poner anime','ponte anime'])
    historial = sinonimar(comando_de_audio,['abrir historial','el historial','un historial'])
    escritorio = sinonimar(comando_de_audio,['escritorio','ve al escritorio','al escritorio','abrir escritorio'])
    windows = sinonimar(comando_de_audio,['windows','win','windel','window'])
    cerrarProg = sinonimar(comando_de_audio,['cerrar programa','cierra programa','cierra el programa','ciérralo','cierralo'])
    alfred = sinonimar(comando_de_audio,['alfred','alfredo','alfre'])


    if verVideo:
        fn.abrirYoutube(comando_de_audio)
    elif blocNota:
        fn.abrirNotas()
    elif terminar:
        fn.terminarALFRED()
    elif itlaVirtual:
        fn.abrirVirtual()
    elif buscarGoogle:
        fn.busqueda()
    elif busquedaAuto:
        fn.busquedaA(comando_de_audio)
    elif cerrarVent:
        fn.cerrarVentana(comando_de_audio)
    elif abrirVent:
        fn.abrirVentana(comando_de_audio)
    elif musica:
        fn.escucharMusica()
    elif escribe:
        fn.escribir(comando_de_audio)
    elif espacio:
        fn.funcionesPress('space')
    elif enter:
        fn.funcionesPress('enter')
    elif pausarResumir:
        fn.funcionesHotkey('fn','playpause')
    elif sigMusica:
        fn.funcionesPress('nexttrack')
    elif antMusica:
        fn.funcionesPress('prevtrack')
    elif cambiarProg:
        fn.funcionesHotkey('alt','tab')
    elif cerrarProg:
        fn.funcionesHotkey('alt','f4')
    elif cambiarPest:
        fn.funcionesHotkey('ctrl','tab')
    elif pelicula:
        fn.verPelicula()
    elif anime:
        fn.verAnime()
    elif historial:
        fn.funcionesHotkey('ctrl','h')
    elif escritorio:
        fn.funcionesHotkey('win','d')
    elif windows:
        fn.funcionesPress('win')
    elif alfred:
        fn.llamarAlfred()






