

label ir_hombre:
    "Pedro se levantó y se dirigió hacia donde estaba el hombre."
    "Al asumarse, pedro miro a un hombre alto y de aspecto misterioso."
    "Vestido de manera elegante y con un sombrero de copa."
    hombre_misterioso "¡Hola! ¿Eres Pedro?"
    pedro "¡Sí! ¿En qué puedo ayudarte?"
    hombre_misterioso "Soy representante del sat y vine a decirte que no has hecho tu declaración anual."
    pedro "carambolas!!!! no sabia nada sobre eso."
    hombre_misterioso "Asi es amigo tener de enemigo al sat es como tener como enemigo a batman y superman juntos."
    hombre_misterioso "Pero no te preocupes, te dire lo que tienes que hacer."
    pedro "Muchas gracias, ¿Qué tengo que hacer?"
    hombre_misterioso "Solo tienes que superar dos desafios."
    hombre_misterioso "El primer desafio es cruzar el puente en obra negra de la muerte."
    pedro "Suena algo peligroso."
    hombre_misterioso "Pero eso no es lo mas peligroso, lo mas peligroso es la espera de la muerte."
    hombre_misterioso "Tendras que poner a prueba tu habilidad y resistencia esperando."
    pedro "Muy bien, suena a un buen desafio."
    hombre_misterioso "Asi es mi estimado, es una aventura llena de desafios, misterio, accion y aventura."
    hombre_misterioso "A si que buena suerte."

    $ deciciones = "lonche"

    hide bg

    jump inicio_viaje

label descansar:
    "Pedro se quedo recostado"
    pedro "An de ser los vendedores de television por cable, mejor me quedare acostado."
    $ renpy.music.set_volume(0.2, channel='music')
    play music "sonidos/explosion.mp3"

    window hide
    
      
    $ music_duration = 7  # Duración en segundos (ajustar al tiempo de la música)
    $ renpy.pause(music_duration, hard=True)  # Hacer una pausa
    stop music  # Detener la música con un fadeout de 5 segundos
    
    window show
    
    pedro "Que fue esa explocion tan fuerte."
    pedro "Creo que llegaron los Aliens."
    honbre_misterioso "Ningun alien solo soy yo, el trabajador del sat."
    hombre_misterioso "Pense que en este lugar tenian educacion"
    hombre_misterioso "Pero solo vengo a decirte que no has hecho tu declaracion anual ante el sat."
    pedro "chintrolas!!!! no sabia nada sobre eso."
    hombre_misterioso "Por tu falta de educacion no te dire de que seran tus dos desafios."
    honbre_misterioso "solo te dire que tienes que ir al reino de mexico y llegar al sat adios"

    # el hombre desaparece 
    pedro "Que raro, bueno a dormir que mañana tenemos que echarle ganas." 

    jump inicio_viaje
