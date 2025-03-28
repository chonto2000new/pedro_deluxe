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


#characters

default pedro = Character("Pedro")
default hijo_p = Character("Hijo de Pedro")
default hombre_misterioso = Character("Hombre Misterioso")
default es = Character("Esposa de pedro") 

label start:

    "como funciona los arreglos de diccionarios"

    "agregar un objeto a un arreglo"


    $ inventario.append({"objeto": "lonche","tipo":"comida", "IsClave": False})
    $ inventario.append({"objeto": "coca-cola","tipo":"comida", "IsClave": False})
    $ inventario.append({"objeto": "pinga","tipo":"comida", "IsClave": True})

    "Mi inventario tiene los siguientes objetos: [inventario[0]['objeto']]"
    "Mi inventario tiene los siguientes objetos: [inventario[1]['objeto']]"

    "buscar un objeto"

    $ encontre = buscar_objeto("lonche")
    "Encontre el objeto [encontre['objeto']]"

    $ encontreNoClave = buscar_objeto_no_clave()

    "tengo un random entre 0 a 2 [numero_random(encontreNoClave)]"
    "tengo un random entre 0 a 2 dos [numero_random(encontreNoClave)]"

    $ random = numero_random(encontreNoClave)

    "Encontre el objeto en mi arreglo [encontreNoClave[random]['objeto']] , [encontreNoClave[1]['objeto']] "


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
