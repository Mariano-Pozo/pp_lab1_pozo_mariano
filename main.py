#Pozo, Mariano Leonel
import re
import json

with open('C:\\Users\\Inoue\\Desktop\\carpet\\Programacion_I\\Parcial\\dt.json') as archivo:
    data_nba = json.load(archivo)
          
lista_nba = data_nba["jugadores"]

def mostrar_jugadores(lista):
    for jugador in lista:
        print("{} - {}".format(jugador["nombre"],jugador["posicion"]))

def mostrar_estadistica(lista):
    cantidad = len(lista)
    indice_ingresado = int(input("Ingresar indice del jugador para ver sus estadisticas: "))
    while indice_ingresado > cantidad or indice_ingresado < 0:
        indice_ingresado = int(input("Ingresar indice valido del jugador para ver sus estadisticas"))

def ingresar_opcion(opciones: list)-> str:
    while True:
        opcion = input("Igresar una de las siguientes opciones:  {opciones}").lower()
        if opcion not in opciones:
            print("Opcion no valida. Try again")
        else:
            return opcion










