
label camino_piedras:
    $ random_name = "Ladron"

    $ inventario.append({"objeto": "lonche","tipo":"comida", "IsClave": False, "img": "inventario/lonche.png"})

    pedro "Me armaré de valor y tomaré el camino de piedras."
    pedro "Que tanto es volar entre los arboles y saltar algunas piedras."
    "Al adentrarse un poco en este camino pedro escucho una voz"
    personaje_random "pss pss"
    personaje_random "oye tu"
    personaje_random "si tu"
    pedro "quien anda ahi"
    personaje_random "ya te la sabes celular y cartera"
    $ random_name = "Ladron"
    pedro "no por favor no se lleve mis perteencias"
    personaje_random "con que pertenencias eh jajajajaj"
    personaje_random "eso es lo que me gusta las pertenencias de los demas"
    pedro "creo que deberia de"
    menu:
        "darle una de tus pertenencias":
            jump dar_objeto
        "correr":
            jump correr

    label dar_objeto:
        $ buscar_pertenencia = buscar_objeto_no_clave()

        $ random = numero_random(buscar_pertenencia)

        $ pertenencia_a_dar = buscar_pertenencia[random]['objeto']

        pedro "Bueno, no me queda de otra, te daré [pertenencia_a_dar]."
        personaje_random "gracias"
        personaje_random "ahora lo vendere y comprare un foco jajajajaj adios"
        "El ladron se fue corriendo con [pertenencia_a_dar]"
        $ inventario = quitar_objeto_inventario(pertenencia_a_dar)
        pedro "No mi [pertenencia_a_dar]"
        pedro "Bueno al menos ya llegue al final del camino"
        pedro "Eso fue muy rapido"
        jump salir_camino_uno

    label correr:
        pedro "Bueno si mira yo"
        "Pedro comienza a correr con todas sus fuerzas"
        personaje_random "No corras ya te tengo en la mira"
        pedro "Rayos tengo que pensar si me voy a la izquierda o derecha"
        pedro "Parece que a la derecha solo estan un par de hojas y a la izquierda tendria que salrtar un barranco"
        menu:
            "ir a la izquierda":
                jump izquierda
            "ir a la derecha":
                jump derecha
        label izquierda:
            pedro "Voy a saltar el barranco"
            "Pedro salta el barranco y cae exitosamente al otro lado"

            personaje_random "no es como si yo no pudiera hacer lo mismo"

            "El ladron salta epicamente"
            "Pero no logra llegar al otro lado"
            personaje_random "haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            pedro "Bueno uno menos"
            pedro "Bueno al menos ya llegue al final del camino"
            pedro "Eso fue muy rapido"
            jump salir_camino_uno

        label derecha:
            pedro "Voy a la derecha"
            "Pedro corre hacia la derecha"
            pedro "Bueno se ve que el camino esta libre"
            "pero al pisar las hojas cae por un gujero"
            pedro "haaaaaaaaaaa" 
            pedro "huuuuuuuuuuuuu"
            pedro "hooooooooooooooo"
            "pfffff"
            pedro "Rayos si que estaba profundo"
            personaje_random "Bueno parece que ahora necesitas ayuda, si me das uno de tus objetos te ayudare a salir"
            "El ladron ayuda a pedro a salir del hoyo"
            $ buscar_pertenencia = buscar_objeto_no_clave()

            $ random = numero_random(buscar_pertenencia)

            $ pertenencia_a_dar = buscar_pertenencia[random]['objeto']

            $ inventario = quitar_objeto_inventario(pertenencia_a_dar)

            pedro "Gracias, bueno aqui tienes mi [pertenencia_a_dar]"
            personaje_random "gracias"
            personaje_random "ahora lo vendere y comprare un foco jajajajaj adios"
            pedro "Bueno al menos ya llegue al final del camino"
            jump salir_camino_uno


    

    
    


label camino_flores: