init python:
    def buscar_objeto(nombre_objeto):
        return next((obj for obj in inventario if obj["objeto"] == nombre_objeto), None)

    def buscar_objeto_no_clave():
        return list(filter(lambda obj: obj["IsClave"] == False, inventario))

    def numero_random(un_arreglo):
        numero_final = len(un_arreglo) - 1
        return renpy.random.randint(0, numero_final)

    def quitar_objeto_inventario(nombre_objeto):
        return list(filter(lambda obj: obj["objeto"] != nombre_objeto, inventario))

  
