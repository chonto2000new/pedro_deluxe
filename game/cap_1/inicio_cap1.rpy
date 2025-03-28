label inicio_cap1:

    image bg casa = Transform("bg_casa.png", size=(1920, 1200))


    scene bg casa

    with fade

    "Érase una vez un hombre llamado Pedro, que vivía en las orillas del reino de México."

    "Pedro era un granjero honesto y trabajador, además de tener una gran familia muy unida que le ayudaba con el cuidado y mantenimiento de la granja."

    "Pedro y su familia eran felices, puesto que todos los alimentos que consumían venían de su propia cosecha, además de obtener ganancias por ellos."

    image pedro = "images/characters/pedro/pedro_igle.png"

    show pedro at left
    
    pedro "¡Hola! yo me llamo pedro?"

    "Un día que Pedro estaba descansando en su sillon y recibió el llamado de uno de sus hijos que le comentaba que un hombre lo estaba buscando."

    hijo_p "¡Papá! ¡Un hombre te está buscando!"

    "Pdro no habia podido descansar nada a si que el tomo una decisión."

    menu:
        "ir a ver al hombre":
            jump ir_hombre
        "descansar":
            jump descansar

    return
