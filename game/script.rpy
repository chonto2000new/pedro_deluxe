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


#characters

default pedro = Character("Pedro")
default hijo_p = Character("Hijo de Pedro")
default hombre_misterioso = Character("Hombre Misterioso")
default es = Character("Esposa de pedro") 

label start:
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
