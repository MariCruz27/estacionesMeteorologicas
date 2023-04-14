import random
import calendar
from tda_tabla_hash import crear_tabla, funcion_hash
from tda_lista import Lista
from funciones_especiales import insertarEstacion
import datetime



estados = ["soleado", "nublado", "lloviendo", "nevado"]

def crear_estacion(pais, latitud, longitud, altitud):
    """
        Crea una estación climática con la información del país, latitud, longitud y altitud especificados.

        Parámetros:
            - pais (str): El país donde se encuentra la estación.
            - latitud (float): La latitud geográfica de la estación.
            - longitud (float): La longitud geográfica de la estación.
            - altitud (float): La altitud de la estación.

        Retorno:
            - lista: Una lista que contiene el nombre del país, un diccionario con las coordenadas geográficas y un diccionario vacío para almacenar los datos de los diferentes meses del año.
    """
    coordenadas = {"latitud": latitud, "longitud": longitud, "altitud": altitud, "id": latitud + longitud + altitud}
    estacion = [pais, coordenadas,  {"January": [], "February": [], "March": [], "April": [], "May": [], "June": [], "July": [], "August": [], "September": [], "October": [], "November": [], "December": []}]

    return estacion

def crear_estacion_manual():
    pais = input("Ingresa el país de la estación\n")
    latitud = int(input("Ingresa la latitud de la estación\n"))
    longitud = int(input("Ingresa la longitud de la estación\n"))
    altitud = int(input("Ingresa la altitud de la estación\n"))
    estacion = crear_estacion(pais, latitud, longitud, altitud)
    return estacion

def agregar_estacion(tabla, estacion):
    """
        Agrega una estación a la tabla hash especificada.

        Parámetros:
            - tabla (list): Una tabla hash para almacenar la información de las diferentes estaciones.
            - estacion (list): Un objeto de estación que se agregará a la tabla hash.

        Retorno:
            None
    """
    posicion = funcion_hash(estacion[0], len(tabla))
    if tabla[posicion] is None:
        tabla[posicion] = Lista()
    insertarEstacion(tabla[posicion], estacion)

def convetir_meses_a_ingles(mes):
    """
        Convierte el nombre de un mes en español al correspondiente en inglés.

        Parámetros:
            - mes (str): El nombre de un mes en español.

        Retorno:
            str: El nombre del mes correspondiente en inglés.
    """
    if mes.lower() == "enero":
        return "January"
    elif mes.lower() == "febrero":
        return "February"
    elif mes.lower() == "marzo":
        return "March"
    elif mes.lower() == "abril":
        return "April"
    elif mes.lower() == "mayo":
        return "May"
    elif mes.lower() == "junio":
        return "June"
    elif mes.lower() == "julio":
        return "July"
    elif mes.lower() == "agosto":
        return "August"
    elif mes.lower() == "septiembre":
        return "September"
    elif mes.lower() == "octubre":
        return "October"
    elif mes.lower() == "noviembre":
        return "November"
    elif mes.lower() == "diciembre":
        return "December"
    

def llenar_registros_anuales(estacion):
    """
        Actualiza los registros anuales de una estación con datos aleatorios.

        La función genera un registro para cada hora del día en que se hizo la medición. Para cada registro, se genera información
        aleatoria sobre la temperatura, presión, humedad y el clima. Además, se registra el día y la hora en que se hizo la medición.

        Parámetros:
            - estacion (list): Un objeto de estación que se actualizará con los nuevos registros.

        Returns:
            None
    """
    limpiar_registros(estacion)
    for mes in estacion[2]:
        year = 2023
        _, dias_mes = calendar.monthrange(year, list(calendar.month_name).index(mes))
        for dia in range(1, dias_mes+1):
            numero_registro = random.randint(0, 24) 
            for registro in range(numero_registro):
                hora = random.randint(0, 23)
                minutos = random.randint(0, 59)
                hora_minutos = f"{hora}:{minutos}"
                temperatura = random.uniform(15, 40) 
                presion = random.randint(980, 1040) 
                humedad = random.randint(0, 100)
                clima = estados[random.randint(0, len(estados)-1)]
                estacion[2][mes].append({'dia': dia, 'hora': hora_minutos, 'temperatura': temperatura, 'presion': presion, 'humedad': humedad, 'clima': clima})

def pedirFecha():
    anho = int(input("Ingresa el año: "))
    mes = int(input("Ingresa el mes: "))
    dia = int(input("Ingresa el día: "))
    hora = int(input("Ingresa la hora: "))
    minutos = int(input("Ingresa los minutos: "))

    fecha = datetime.datetime(anho, mes, dia, hora, minutos, 0)

    # Formato de la fecha ingresada
    fecha_formato = fecha.strftime("%Y-%m-%d %H:%M:%S")
    return fecha_formato,dia,hora,minutos

def agregar_registro(estacion, mes):
    bandera = True
    while bandera:
        fecha_registro,dia,hora,minutos  = pedirFecha()
        hoy = datetime.datetime.now()
        hoy_formato = hoy.strftime("%Y-%m-%d %H:%M:%S")
        if(fecha_registro < hoy_formato):
            print("Fecha Invalida")
            bandera = False
    temp = input("\nIngresa la temperatura: ")
    hum = input("Ingresa la humedad: ")
    pre = input("Ingresa la presión")
    print("soleado - nublado - lloviendo - nevado")
    clima = input("Ingresa el estado del clima: ")
    hora_minutos = f"{hora}:{minutos}"
    estacion[2][mes].append({'dia': dia, 'hora': hora_minutos, 'temperatura': temp, 'presion': pre, 'humedad': hum, 'clima': clima})


def limpiar_registros(estacion):
    """
        Borra todos los registros existentes en un objeto de estación.

        La función itera a través de los meses en el diccionario de registros de la estación y llama al método clear en cada lista de registros
        para eliminarlos.

        Parámetros:
            - estacion (list): Un objeto de estación que se limpiará de registros.

        Returns:
            None
    """
    for mes in estacion[2]:
        estacion[2][mes].clear()


def promedio_temperatura_humedad(estacion, mes):
    """
        Calcula el promedio de temperatura y humedad para un mes específico de una estación.

        La función itera a través de todos los registros de ese mes en la estación y suma las temperaturas y humedades de cada registro.
        Luego divide estas sumas por el número total de registros en el mes para obtener los promedios.

        Parámetros:
            - estacion (list): Un objeto de estación que contiene registros mensuales de temperatura y humedad.
            - mes (str): El mes para el cual se calcula el promedio de temperatura y humedad. Debe ser una cadena de texto en español.

        Retorno:
            - tupla: Una tupla que contiene dos valores, el promedio de temperatura y el promedio de humedad para el mes especificado.
    """

    promedio_temperatura = 0
    promedio_humedad = 0
    for registro in estacion[2][mes]:
        promedio_temperatura += registro['temperatura']
        promedio_humedad += registro['humedad']
    if len(estacion[2][mes]) > 0:
        promedio_temperatura /= len(estacion[2][mes])
        promedio_humedad /= len(estacion[2][mes])
        return promedio_temperatura, promedio_humedad
    else:
        return 0, 0

def buscar_estaciones(tabla, clima):
    """
        Esta función recibe una tabla hash y un tipo de clima y devuelve una nueva tabla hash que contiene todas las estaciones
        que tienen registros con el clima indicado.
    
        Parámetros:
            - tabla (list): una tabla hash que contiene estaciones como valores.
            - clima (str): una cadena que representa el clima que se busca en los registros de las estaciones.
    
        Retorno:
            - tabla_aux: una nueva tabla hash que contiene las estaciones que tienen registros con el clima indicado.
    """
    tabla_aux = crear_tabla(len(tabla))
    for lista in tabla:
        bandera = False
        if lista is not None:
            aux = lista.inicio
            while aux is not None:
                estacion = aux.info
                for mes in estacion[2]:
                    for registro in estacion[2][mes]:
                        if registro['clima'] == clima:
                            agregar_estacion(tabla_aux, estacion)
                            bandera = True
                            break  # rompe el ciclo de iteración de registros
                    if bandera:
                        break  # rompe el ciclo de iteración de meses
                aux = aux.sig
    return tabla_aux

def imprimir_estaciones_con_coordenadas(tabla):
    """
        Imprime en pantalla todas las estaciones en la tabla con sus correspondientes coordenadas geográficas.

        Parámetros:
            - tabla (list): Una lista que representa una tabla hash donde se encuentran almacenadas las estaciones.
    
        Retorno:
            - No retorna ningún valor, solamente imprime el resultado.
    """
    for lista in tabla:
        if lista is not None:
            cont = 0
            aux = lista.inicio
            print("\nEstaciones de ", aux.info[0])
            while aux is not None:
                cont += 1
                estacion = aux.info
                print(f"Estacion {cont}:  - Coordenadas: latitud = {estacion[1]['latitud']}, longitud = {estacion[1]['longitud']}, altitud = {estacion[1]['altitud']}")
                aux = aux.sig

def llenar_todos_los_registros(tabla):
    """
        Llena los registros anuales de todas las estaciones presentes en la tabla de hash.

        Parámetros:
            - tabla (list): La tabla de hash que contiene las estaciones.

        Retorno:
            None
    """
    for lista in tabla:
        if lista is not None:
            aux = lista.inicio
            while aux is not None:
                estacion = aux.info
                llenar_registros_anuales(estacion)
                aux = aux.sig

def imprimir_promedio_temperatura_humedad(tabla, mes):
    """
        Imprime el promedio de temperatura y humedad de todas las estaciones de la tabla en el mes dado.

        Parámetros:
            - tabla (list): Una lista que representa una tabla hash donde se encuentran almacenadas las estaciones.
            - mes (str): representa el mes a consultar (Ejemplo: "enero", "febrero", etc.).

        Retorno:
            - No retorna ningún valor, solamente imprime el resultado.
    """
    for lista in tabla:
        if lista is not None:
            cont = 0
            aux = lista.inicio
            print("\nEstaciones de ", aux.info[0])
            while aux is not None:
                cont += 1
                estacion = aux.info
                promedio_temperatura, promedio_humedad = promedio_temperatura_humedad(estacion, mes)
                print(f"Estacion: {cont} - Temperatura: {promedio_temperatura:.2f} - Humedad: {promedio_humedad:.2f}")
                aux = aux.sig
                


