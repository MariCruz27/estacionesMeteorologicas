from tda_lista import nodoLista

def insertarEstacion(lista, dato):
    """  
        Inserta una estación en una lista ordenada según su id. El id de una estación se calcula como la suma de su latitud, longitud y altitud.

        Args:
            lista (Lista): La lista donde se insertará la estación.
            dato (list): La estación que se insertará en la lista.

        Returns:
            None. 
    """
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None) or (lista.inicio.info[1]["id"] > dato[1]["id"]):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while(act is not None and act.info[1]["id"] < dato[1]["id"]):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1