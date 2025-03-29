default player = {
"hp": 100,
"mp": 50,
"nivel": 1
}
# default mp = 50
# default nivel = 1
default enemigo_hp = 100
default accion_texto = ""
default turno_activo = False
default background_battle = "videos/battle_bg.webm"
default viajeRapido = ""
default deciciones = ""
default inventario = []
default random_name = "Personaje Random"


#characters

default pedro = Character("Pedro")
default hijo_p = Character("Hijo de Pedro")
default hombre_misterioso = Character("Hombre Misterioso")
default es = Character("Esposa de pedro") 
default personaje_random = Character("[random_name]") 

label start:

    # "como funciona los arreglos de diccionarios"

    # "agregar un objeto a un arreglo"


    # $ inventario.append({"objeto": "lonche","tipo":"comida", "IsClave": False, "img": "lonche.png"})
    # $ inventario.append({"objeto": "coca-cola","tipo":"comida", "IsClave": False,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})
    # $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True,"img": "lonche.png"})

    # "Mi inventario tiene los siguientes objetos: [inventario[0]['objeto']]"
    # "Mi inventario tiene los siguientes objetos: [inventario[1]['objeto']]"

    # "buscar un objeto"

    # $ encontre = buscar_objeto("lonche")
    # "Encontre el objeto [encontre['objeto']]"

    # $ encontreNoClave = buscar_objeto_no_clave()

    # "tengo un random entre 0 a 2 [numero_random(encontreNoClave)]"
    # "tengo un random entre 0 a 2 dos [numero_random(encontreNoClave)]"

    # $ random = numero_random(encontreNoClave)

    # "Encontre el objeto en mi arreglo [encontreNoClave[random]['objeto']] , [encontreNoClave[1]['objeto']] "


    "¡Comienza el combate!"
    menu: 
            "jugar combate":
                jump start_combate
            "iniciar la historia":
                    jump inicio_cap1
            "viaje":
                jump viaje
label viaje:
    $ viajeRapido = renpy.input("¿A dónde quieres viajar?")
    `¡Te diriges a [viajeRapido]!`
    jump expression  viajeRapido 



# Obtener el tamaño de la pantalla
default screen_width = config.screen_width
default screen_height = config.screen_height

# Variable de inventario con imágenes de objetos

# Pantalla de la mochila
screen mochila():
    modal True  # Bloquea clics fuera de la mochila

    # Fondo semitransparente
    add Transform("gui/overlay/black.png", alpha=0.7)

    frame:
        background Frame("gui/textbox.png", 20, 20)
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        # Definir el tamaño de los ítems
        $ item_size = 50  # Ancho y alto de cada ícono
        $ columnas = max(2, screen_width // (item_size + 1500))  # Mínimo 1 columna
        $ filas = (len(inventario)  + columnas - 1) // columnas  # Calcula el número de filas

        grid filas columnas:
            spacing 10
            for item in inventario:
                add Transform(item['img'], xsize=item_size, ysize=item_size)

        # Botón para cerrar la mochila
        textbutton "Cerrar" action Hide("mochila") xalign 0.5 yalign 1.0

# Pantalla con el botón de la mochila
screen boton_mochila():
    imagebutton:
        idle "mochila_idle.png"
        hover "mochila_hover.png"
        action Show("mochila")
        xalign 0.95
        yalign 0.05

# Hacer que el botón de la mochila siempre esté visible
init python:
    config.overlay_screens.append("boton_mochila")
