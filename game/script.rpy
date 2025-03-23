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

#characters

default pedro = Character("Pedro")
default hijo_p = Character("Hijo de Pedro")

label start:
    "¡Comienza el combate!"
    menu: 
            "jugar combate":
                jump start_combate
            "iniciar la historia":
                    jump inicio_cap1 
     
