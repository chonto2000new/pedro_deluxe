label inicio_viaje:



    "Al dia siguiente pedro se desperto y se preparo para su viaje."
    es "Pedro hice un lonche para tu viaje."

    if deciciones == "lonche":
        es "Aqui tienes tu lonche."
        es "Ten cuidado en tu viaje."
        pedro "Gracias, con este lonche de huevo con chorizo tendre mucho poder  en mi viaje."
       
    else:
        es "Aqui tienes tu lonche."
        pedro "no muchas gracias, creo que ire rapido a si que para la hora de la comida ya estare aqui."


    "Pedro se despidio de toda su familia y se dirigio a la puerta de su casa."
    "Pedro comenzo a caminar y poco a poco su casa se fue desbaneciendo ya que el se dirigia hacia el bosque."
    "Al entrar al bosque pedro vio un camino lleno de arboles piedras y plantas."
    "Pero del otro lado pedro miro un camino lleno de flores y arboles frondosos."
    "Lo malo es que el camino lleno de flores era muy largo y el camino lleno de piedras era muy corto."
    "Pedro tenia que tomar una decision."

    menu:
        "Tomar el camino de piedras":
            jump camino_piedras
        "Tomar el camino de flores":
            jump camino_flores
