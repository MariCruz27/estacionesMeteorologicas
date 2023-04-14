from piases import *
from funciones import *
from tda_tabla_hash import *
from tda_lista import *
import os
from datetime import datetime

def menu():
    print("=================================================")
    print("> [1] - Agregar estación.\n> [2] - Ver estaciones meteorologicas por pais.\n> [3] - Registrar clima a una estación.\n> [4] - Promedio de temperatura y humedad.\n> [5] - Buscar estaciones por clima.\n> [0] - Salir.")
    print("=================================================\n")
    opcion = int(input("Ingrese una opcion: "))
    return opcion


tablaEstaciones = crear_tabla(10)

for estaciones in range(0,3):
    estacion = crear_estacion(elegir_pais(), random.uniform(-90, 90), random.uniform(-180, 180), random.randint(0, 1000))
    agregar_estacion(tablaEstaciones, estacion)
    llenar_todos_los_registros(tablaEstaciones)

respuesta = menu()
while respuesta != 0:
    if respuesta == 1:
        print("Registro de una estación.")
        estacion = crear_estacion_manual()
        agregar_estacion(tablaEstaciones, estacion)
        print("Estación registrada con exito")
    elif respuesta == 2:
        print("Estacion meteorologica por pais.")
        imprimir_estaciones_con_coordenadas(tablaEstaciones)
    elif respuesta == 3:
        print("Registro de clima por estaciones.")
        pais = input("Ingresa el pais de la estación")
        id = input("Ingresa el ID de la estación")
        #estacion = buscarEstación
        print("Ingresa el mes en letras")
        agregar_registro(estacion)
        print("Registros llenados con exito.")
    elif respuesta == 4:
        print("Promedio de temperatura y humedad.")
        mes = input("Ingrese el mes: ")
        mes_ingles = convetir_meses_a_ingles(mes)
        imprimir_promedio_temperatura_humedad(tablaEstaciones, mes_ingles)
    elif respuesta == 5:
        print("Buscar estaciones por clima.")
        clima = input("Ingrese el clima: ")
        estaciones_clima = buscar_estaciones(tablaEstaciones, clima)
        imprimir_estaciones_con_coordenadas(estaciones_clima)
    else:
        print("Opcion incorrecta.")
    input("Presione enter para continuar...")
    os.system("cls")
    respuesta = menu()

    


