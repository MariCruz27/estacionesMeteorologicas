import random

lista_paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Surinam", "Uruguay", "Venezuela"]

def elegir_pais():
    """
        Devuelve un país aleatorio de la lista de países predefinida.

        Retorno:
            - str: El nombre del país elegido aleatoriamente.
    """
    return lista_paises[random.randint(0, len(lista_paises)-1)]
