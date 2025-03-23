# Pantalla del combate con botones y texto
screen rpg_calculator_buttons():
    # Información de estadísticas del jugador
    frame:
        align (0.5, 0.7)  # Centra el frame en la pantalla
        padding (10, 10)  # Espacio dentro del frame
        vbox:
            text "HP: [player['hp']]" size 22 color "#ff3333"
            text "MP: [player['mp']]" size 22 color "#3333ff"
            text "Nivel: [player['nivel']]" size 22 color "#fff"
    
    # Botones para las acciones del combate
    
    

    frame:
        align (0.0, 1.0)  # Esquina inferior izquierda
        padding (20, 20)  # Espacio dentro del frame
        background "#1f1e1ecc"
        grid 2 2 spacing 100:  # 2 columnas x 2 filas
            textbutton "Atacar" action [Function(actualizar_turno, "atacar"), Return("atacar")] sensitive (not turno_activo)
            textbutton "Habilidad" action [Function(actualizar_turno, "habilidad"), Return("habilidad")] sensitive (not turno_activo)
            textbutton "Objeto" action [Function(actualizar_turno, "objeto"), Return("objeto")] sensitive (not turno_activo)
            textbutton "Huir" action [Function(actualizar_turno, "huir"), Return("huir")] sensitive (not turno_activo)

    # Espacio para el texto de acción
    frame:
        xpos 0.245  # Alineado al borde izquierdo
        ypos 0.777  # Alineado al borde superior
        xsize 1449  # Ancho fijo de 400 píxeles
        ysize 250  # Alto fijo de 200 píxeles
        padding (10, 10)  # Espacio dentro del frame
        background "#333c"  # Fondo del frame
        text "[accion_texto]" size 40 color "#fff"  # Texto dentro del frame

# Funciones de combate
init python:
    # Variables del jugador y enemigo
    # hp = 100
    # mp = 50
    # nivel = 1

    # player = {
    #     hp: 100,
    #     mp: 50,
    #     nivel: 1

    # }
    # enemigo_hp = 100

    # Variable para almacenar el texto de las acciones
    accion_texto = ""

    # Variable para controlar si el turno está activo
    turno_activo = False

    # Función para actualizar el turno
    def actualizar_turno(accion):
        global turno_activo, resultado
        turno_activo = True  # Deshabilitar los botones
        if accion == "atacar":
            resultado = atacar()
        elif accion == "habilidad":
            habilidad()
        elif accion == "objeto":
            objeto()
        elif accion == "huir":
            huir()

    # Función de ataque
    def atacar():
        global player, enemigo_hp, accion_texto
        enemigo_hp -= 10  # Daño de ataque
        accion_texto = f"Atacas al enemigo y le haces 10 de daño. Enemigo HP: {enemigo_hp}"
        if enemigo_hp <= 0:
            enemigo_hp = 0
            accion_texto += "\n¡Has derrotado al enemigo!"
            return "victoria"  # Retornamos un valor para manejar después
        else:
            return golpeado(5)  # El enemigo golpea al jugador
            

    # Función para ser golpeado
    def golpeado(dano):
        global player, accion_texto
        player['hp'] -= dano
        accion_texto += f"\nEl enemigo te golpea y pierdes {dano} HP. Tu HP: {player['hp']}"
        if player['hp'] <= 0:
            accion_texto += "\n¡Has sido derrotado!"
            return "derrota"  # Retornamos un valor para manejar después
        return None

    # Función para habilidad
    def habilidad():
        global accion_texto
        accion_texto = "¡Usas una habilidad especial!"
        return None
    
    # Función para objeto
    def objeto():
        global accion_texto
        accion_texto = "Abres tu bolsa de objetos y tomas una poción."
        return None

    # Función para huir
    def huir():
        global accion_texto
        accion_texto = "Intentas huir, pero no puedes escapar."
        return None

# Etiquetas para el flujo del combate
label start_combate:
    # Inicializamos las variables y comenzamos el combate
    # default hp = 100
   
    

    show expression Movie(channel="movie", play=background_battle, loop=True, size=(config.screen_width, config.screen_height)) onlayer master

   


    # Ocultamos la ventana de texto (esto es clave para evitar que avance el texto)
    window hide

    "¡Comienza el combate!"
    "Haz tu movimiento en el combate, selecciona un ataque, habilidad, objeto o huir."

    label buena_suerte:
        "Buena suerte."

        play music "audio/music/battle_theme_one.ogg" loop

    # Bucle del combate
    label combate:

        # show expression Movie(channel="movie", play="videos/battle_bg.webm", loop=True, size=(config.screen_width, config.screen_height)) onlayer master
        # Llamamos a la pantalla de combate y manejamos el resultado
        call screen rpg_calculator_buttons
        # $ accion = _return  # Capturamos el valor retornado por la pantalla

        # Mostramos el resultado de la acción
        show screen rpg_calculator_buttons  # Mostramos la pantalla de nuevo
        pause 3.0  # Pausa para que el jugador lea el mensaje


        # Verificamos si el combate ha terminado
        if resultado == "victoria":
            stop music fadeout 5.0
            # Detener el video en el canal 'movie'
            stop movie  # Esto detendrá la reproducción del video.
            hide expression Movie(channel="movie", play=background_battle, loop=True, size=(config.screen_width, config.screen_height)) onlayer master
            jump victoria
        elif resultado == "derrota":
            stop music fadeout 5.0
            # Detener el video en el canal 'movie'
            stop movie  # Esto detendrá la reproducción del video.
            hide expression Movie(channel="movie", play=background_battle, loop=True, size=(config.screen_width, config.screen_height)) onlayer master
            jump derrota

        # Turno del enemigo
        $ accion_texto = "El enemigo está preparando su ataque..."
        show screen rpg_calculator_buttons  # Mostramos la pantalla de nuevo
        pause 3.0  # Pausa para simular el turno del enemigo

        # El enemigo ataca
        $ resultado = golpeado(5)  # El enemigo hace 5 de daño
        show screen rpg_calculator_buttons  # Mostramos la pantalla de nuevo
        pause 3.0  # Pausa para que el jugador lea el mensaje

        # Verificamos si el combate ha terminado
        if resultado == "victoria":
            stop music fadeout 5.0
            # Detener el video en el canal 'movie'
            stop movie  # Esto detendrá la reproducción del video.
            hide expression Movie(channel="movie", play=background_battle, loop=True, size=(config.screen_width, config.screen_height)) onlayer master
            jump victoria
        elif resultado == "derrota":
            stop music fadeout 2.0
            stop movie fadeout 5.0 # Esto detendrá la reproducción del video.
            hide expression Movie(channel="movie", play=background_battle, loop=True, size=(config.screen_width, config.screen_height)) onlayer master
            jump derrota

        # Habilitar los botones nuevamente
        $ turno_activo = False

        # Volvemos al bucle del combate
        jump combate

label victoria:
    # Este es el flujo después de que el jugador gane el combate
    hide screen rpg_calculator_buttons
    window auto  # Restauramos la ventana de texto
    "¡Victoria!"
    return

label derrota:
    # Este es el flujo después de que el jugador pierda el combate
    hide screen rpg_calculator_buttons
    window auto  # Restauramos la ventana de texto
    "¡Derrota!"
    return