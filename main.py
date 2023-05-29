#Pozo, Mariano Leonel
import re
import json
import os


def clear_console() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls' para borrar la pantalla.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

with open('Parcial\dt.json') as archivo:
    data_nba = json.load(archivo)
          
lista_jugador = data_nba["jugadores"]

#1 ---------------------------------------
def mostrar_jugadores(lista):
    """
    La función "mostrar_jugadores" toma una lista de diccionarios que contienen información de los
    jugadores e imprime sus nombres y posiciones al mismo tiempo que devuelve una lista de los nombres
    de los jugadores.
    
    :param lista: una lista de diccionarios, donde cada diccionario representa a un jugador y contiene
    su nombre y posición
    :return: una lista de nombres de jugadores.
    """
    nombres = []
    for jugador in lista:
        nombres.append(jugador["nombre"])
        print("{} - {}".format(jugador["nombre"],jugador["posicion"]))
    return nombres
#2 ---------------------------------------
def seleccionar_jugador_por_indice(lista_jugadores:list):#punto 2
   """La funcion pide un indice de un jugador y muestra en pantalla sus estadisticas
    admite un dato tipo lista de jugadores
    retorna una lista con el nombre y las estadisticas del jugador solicitado"""
   
   mostrar_indice_jugador(lista_jugadores)
   indice_jugador = int(input("ingrese el el indice de jugador a buscar: "))
   if re.search(r"^[0-9]|1[0-1]$",str(indice_jugador)) != None:
        lista_estadisticas = []
        acumulador_estadisticas = ""
        if len(lista_jugadores) >= 0:      
            nombre_jugador = lista_jugadores[indice_jugador]["nombre"]
            
            lista_estadisticas.append("{}".format(nombre_jugador))
            acumulador_estadisticas = ("{}\n".format(nombre_jugador))
            estadisticas_dict = lista_jugadores[indice_jugador]["estadisticas"]
            for clave,valor in estadisticas_dict.items():
                        formateo =("{0}: {1}".format(clave,valor))
                        formateo_print =("{0}: {1}\n".format(clave,valor))
                        acumulador_estadisticas += formateo_print                                                       
            
                        lista_estadisticas.append(formateo)
   else:
       print("no valido")
    
                   
   print("\n",acumulador_estadisticas)
   return lista_estadisticas #identacion esta rara
           
def mostrar_indice_jugador(lista_jugadores:list):
    """
    imprime los jugadores de una lista con su respectivo indice
    admite un dato tipo lista de jugadores
    no retorna nada
    """
    contador = -1
    for jugador in lista_jugadores:
        contador += 1
        print("{0}.{1}".format(contador,jugador["nombre"]))

#3 ------------------------------------------------------

def guardar_archivo(ruta, datos):
    '''
    Recibe la ruta donde se guardara el archivo, y los datos que seran guardados en esa ruta.
    Sino existe el archivo lo crea.
    Devuelve un mensaje en caso de que se guarde correctamente o no.
    '''

    with open(ruta, "w+") as archivo:
        formato = "\n".join(datos)
        archivo.writelines(formato)
        if formato != "":
            mensaje = f"Se guardo el archivo: {ruta}"
        else: 
            mensaje = f"Error al guardar el archivo {ruta}"  
    return print(mensaje) 

#4 ------------------------------------------------------
# Permitir al usuario buscar un jugador por su nombre y mostrar sus logros,
#  como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
def ingrese_name():    
    """
    Esta función toma una entrada de nombre del usuario y la busca en una lista de diccionarios,
    imprimiendo los logros asociados si los encuentra.
    :return: La función `nombre_logros` está devolviendo el nombre del jugador y sus logros o la cadena
    """
    jugador = input("ingrese nombre")
    return jugador
def nombre_logros(nombre,lista):
    for indice in lista:
        if indice["nombre"].lower() == nombre.lower():
            print(nombre)
            return print(indice["logros"])
        
    print("no encontro")
            

#5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
#Team, ordenado por nombre de manera ascendente.


def ordenar_por_clave(lista: list, clave: str, flag_orden: bool) -> list:
    """
    La función ordena una lista de diccionarios por una clave específica en orden ascendente o
    descendente.
    """
    lista_nueva = lista[:]
    rango_a = len(lista) -1 
    flag_swap = True

    while flag_swap:
        flag_swap = False
        for indice_A in range(rango_a): 
            if (flag_orden == True and lista_nueva[indice_A][clave] > lista_nueva[indice_A+1][clave]) \
                    or (flag_orden == False and lista_nueva[indice_A][clave] < lista_nueva[indice_A+1][clave]):
                lista_nueva[indice_A], lista_nueva[indice_A+1] = lista_nueva[indice_A+1], lista_nueva[indice_A]
                flag_swap = True

    return lista_nueva

def calular_promedio(jugadores:list, primera_clave:str, segunda_clave:str)-> float:
    if jugadores:
        acumulador = 0
        contador = 0
        for jugador in jugadores:
            acumulador += jugador[primera_clave][segunda_clave]
            contador +=1
        if contador > 0:
            promedio = acumulador / contador
            return promedio
    return None

def calcular_imprimir_ordenardenados_alfabeticamente_promedio(lista_jugadores):


    lista_ordenada = ordenar_por_clave(lista_jugadores, "nombre", True)
    promedio = calular_promedio(lista_ordenada,"estadisticas" ,"promedio_puntos_por_partido")
    print(f"El promedio del Equipo es: {promedio}")
    for jugador in lista_ordenada:
        nombre_jugador = jugador["nombre"]
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        mensaje = f"{nombre_jugador}: {promedio_puntos}"
        print(mensaje)


# 6 - Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador
# es miembro del Salón de la Fama del Baloncesto.
def imprimir_key_jugador(jugador_encontrado:dict):
    mensaje = "Error jugador no encontrado"
    
    if jugador_encontrado is not None:
        logros = jugador_encontrado["logros"]
        for logro in logros:
            if logro == "Miembro del Salon de la Fama del Baloncesto":
                mensaje = f"{jugador_encontrado['nombre']}: \n{logro}"
            else: 
                mensaje = "El jugador no es miembro del Salon de la Fama del Baloncesto"

    print(mensaje)

def imprimir_data(dato_a_impirimir):
    print(dato_a_impirimir)

#7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales. 


'''
def calcular_mostrar_rebotes_totales(lista_jugador,primera_clave, segunda_clave)-> dict:
    jugador_maximo = {}
    for indice in range(len(lista_jugador)):
        if indice == 0 or maximo < lista_jugador[indice][primera_clave][segunda_clave]:
            maximo = lista_jugador[indice][primera_clave][segunda_clave]
            jugador_maximo = lista_jugador[indice]
    return jugador_maximo'''

def calcular_mostrar_maximo(lista_jugadores: list[dict], clave_jugador:str, clave_valor:str)-> str:
    """
    La función encuentra el valor máximo de una clave específica en la lista de jugadores y devuelve
    el nombre del jugador que tiene ese valor máximo, junto con el valor mismo, en forma de cadena de texto.
    
    :param jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas
    :param clave_jugador: la clave del diccionario que se utilizará para encontrar el valor máximo
    :param clave_valor: la clave dentro de la clave anterior que se utilizará para obtener el valor específico
    :return: una cadena de texto con el nombre del jugador que tiene el valor máximo de la clave especificada
    y el valor máximo mismo.
    """
    nombre_maximo = None
    maximo = 0
    mensaje = "Error, no se pudo sacar maximo!"
    if lista_jugadores:
        for jugador in lista_jugadores:
            valor = jugador[clave_jugador][clave_valor]
            if nombre_maximo is None or valor > maximo:
                maximo = valor
                nombre_maximo = jugador["nombre"]
        clave_valor = clave_valor.replace("_", " ")
    if nombre_maximo:
        mensaje = "El jugador {0} tiene la mayor cantidad de {1}: {2}.".format(nombre_maximo, clave_valor, maximo)
    return mensaje

#8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo. %

#9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.


#10) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
#más puntos por partido que ese valor.
#11) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
#más rebotes por partido que ese valor.
#12) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
#más asistencias por partido que ese valor.
def solicitar_mostrar_maximo_segun_clave(lista_jugadores, clave):
    valor_ingresado = input("Ingrese el valor que desea buscar: ")

    if re.match("^[0-9]{1,2}$", valor_ingresado): 
        valor_ingresado = int(valor_ingresado)
        clave_normalizada = clave.replace("_", " ")

        for jugador in lista_jugadores:
            if jugador["estadisticas"][clave] > valor_ingresado:
                nombre_encontrado = jugador["nombre"]
                valor_encontrado = jugador["estadisticas"][clave]
                mensaje = f"\n{nombre_encontrado} | {clave_normalizada}: {valor_encontrado}"
                imprimir_data(mensaje)
    else:
        imprimir_data("Valor invalido, ingrese un numero entero.")
#17 Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos

def maxima_cantidad_logros(lista_jugadores):
    valor_maximo = 0

    for jugador in lista_jugadores:
        cantidad_logros = len(jugador["logros"])
        if cantidad_logros > valor_maximo:
            valor_maximo = cantidad_logros
            nombre_jugador_maximo = jugador["nombre"]

    imprimir_data(nombre_jugador_maximo)

# 16 - Calcular y mostrar el promedio de puntos por partido del equipo 
# excluyendo al jugador con la menor cantidad de puntos por partido.
def calcular_promedio(jugadores:list, primera_clave:str, segunda_clave:str)-> float:
    if jugadores: # no sea vacia
        acumulador = 0
        contador = 0
        for jugador in jugadores:
            acumulador += jugador[primera_clave][segunda_clave]
            contador +=1
        if contador > 0:
            promedio = acumulador / contador
            return promedio
    return None

def ordenar_por_clave_doble(lista: list, primera_clave: str, segunda_clave: str, flag_orden: bool) -> list:
    """
    La función ordena una lista de diccionarios por una clave específica en orden ascendente o
    descendente.
    """
    lista_nueva = lista[:]
    rango_a = len(lista) -1 
    flag_swap = True

    while flag_swap:
        flag_swap = False
        for indice_A in range(rango_a): 
            if (flag_orden == True and lista_nueva[indice_A][primera_clave][segunda_clave] > lista_nueva[indice_A+1][primera_clave][segunda_clave]) \
                    or (flag_orden == False and lista_nueva[indice_A][primera_clave][segunda_clave] < lista_nueva[indice_A+1][primera_clave][segunda_clave]):
                lista_nueva[indice_A], lista_nueva[indice_A+1] = lista_nueva[indice_A+1], lista_nueva[indice_A]
                flag_swap = True

    return lista_nueva

def calcular_mostrar_clave_segun_jugador():
    lista_ordenada = ordenar_por_clave_doble(lista_jugador, "estadisticas", "promedio_puntos_por_partido", True)
    del lista_ordenada[0]
    promedio = calcular_promedio(lista_ordenada,"estadisticas" ,"promedio_puntos_por_partido")
    mensaje_promedio = f"El promedio de puntos por partidos sin el peor jugador es: {promedio}"
    imprimir_data(mensaje_promedio)
    for jugador in lista_jugador:
        nombre_jugador = jugador["nombre"]
        valor_encontrado = jugador["estadisticas"]["promedio_puntos_por_partido"]
        mensaje = f"{nombre_jugador}: {valor_encontrado}"
        imprimir_data(mensaje)

#19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas

#20
def validar_opcion_expresion(expresion: str, ingreso_teclado: str) -> int:
    """
    La función valida una entrada de usuario contra una expresión regular y devuelve la entrada como un
    número entero si coincide con la expresión.
    
    :param expresion: un patrón de expresión regular que la entrada del usuario debe coincidir para que
    se considere válido
    :type expresion: str
    :param ingreso_teclado: La cadena de entrada que escribe el usuario. Se compara con el patrón de
    expresión regular especificado en el parámetro "expresión"
    :type ingreso_teclado: str
    :return: un valor entero si la cadena de entrada coincide con el patrón de expresión regular
    especificado en el parámetro "expresión", de lo contrario, devuelve False.
    """

    opcion_validada = False
    if re.match(expresion, ingreso_teclado):
        opcion_validada =int(ingreso_teclado)

    return opcion_validada

def filtrar_jugadores_por_estadistica(lista_jugadores: list[dict], clave_estadistica: str)->list[dict]:
    """
    Esta función filtra una lista de jugadores en función de su promedio de puntos y retorna una lista
    con los jugadores cuyo promedio de puntos es mayor que un valor dado.

    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información como su nombre, edad y puntos promedio por juego
    :param clave_estadistica: La clave de la estadística que se utilizará para filtrar (por ejemplo, "promedio_puntos_por_partido")
    :return: una lista con los jugadores que cumplen la condición
    """
    jugadores_filtrados = []

    valor_ingresado = input("Ingresa un valor: ")
    valor_ingresado = validar_opcion_expresion(r'^[0-9]{1,2}$', valor_ingresado)
    no_encontrado = True

    if valor_ingresado:
        for jugador in lista_jugadores:
            if jugador["estadisticas"][clave_estadistica] > valor_ingresado:
                jugadores_filtrados.append(jugador)
                no_encontrado = False

        if no_encontrado:
            print("No se encontró ningún jugador con más puntos por partido que {0}".format(valor_ingresado))

    return jugadores_filtrados
    
def ordenados_posicion_cancha(lista_jugadores: list[dict])-> None:
    """
    Esta función toma una lista de jugadores, los filtra por su porcentaje de tiros de campo, los ordena
    por su posición en la cancha e imprime su nombre y posición.
    
    :param lista_jugadores: una lista de diccionarios que representan a los jugadores de baloncesto, con
    claves como "nombre" (nombre), "posición" (posición) y "porcentaje_tiros_de_campo" (porcentaje de
    tiros de campo)
    """

    lista_filtrada = filtrar_jugadores_por_estadistica(lista_jugadores,"porcentaje_tiros_de_campo")

    lista_odenada = ordenar_por_clave(lista_filtrada , "posicion", True)

    for jugador in lista_odenada:

        posicion = jugador["posicion"]
        nombre =jugador["nombre"]
        porcentaje_tiros_de_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
      
        print("{0}, {1} porcentaje tiros decampo: {2}".format(posicion, nombre, porcentaje_tiros_de_campo))

def menu():

    while True:
        print("\nMenú de opciones:\n")
        print("1. Mostrar lista de jugadores del Dream Team.")
        print("2. Ver estadísticas completas de un jugador seleccionado.")
        print("3. Guardar estadísticas de un jugador en un archivo .")
        print("4. Buscar un jugador por nombre y mostrar sus logros.")
        print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre.")
        print("6. Verificar si un jugador es miembro del Salón de la Fama del Baloncesto.")
        print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
        print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
        print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
        print("10. Mostrar jugadores que promediaron más puntos por partido que un valor dado.")
        print("11. Mostrar jugadores que promediaron más rebotes por partido que un valor dado.")
        print("12. Mostrar jugadores que promediaron más asistencias por partido que un valor dado.")
        print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
        print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
        print("15. Mostrar jugadores con un porcentaje de tiros libres superior a un valor dado.")
        print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
        print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.")
        print("18. Mostrar jugadores con un porcentaje de tiros triples superior a un valor dado.")
        print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.")
        print("20. Mostrar jugadores ordenados por posición en la cancha con un porcentaje de tiros de campo superior a un valor dado.")
        print("23. Bonus")
        print("21. Exit")

        opcion_deseada = input("\nIngrese la opción deseada: ")
        opcion_deseada = int(opcion_deseada)
        match opcion_deseada:
            case 1:
                mostrar_jugadores(lista_jugador)
            case 2:
                seleccionar_jugador_por_indice(lista_jugador)
            case 3:
                ruta_archivo = "Parcial\data.csv" # jugador_indice_estadistica.csv
                selec_indic = seleccionar_jugador_por_indice(lista_jugador)
                datos_para_guardar = selec_indic
                guardar_archivo(ruta_archivo, datos_para_guardar)
            case 4:
                opcion = mostrar_jugadores(lista_jugador)
                print(opcion)
                nombres_a_elegir = ingrese_name()
                nombre_logros(nombres_a_elegir,lista_jugador)
            case 5:
                calcular_imprimir_ordenardenados_alfabeticamente_promedio(lista_jugador)
            case 6:
                nombre = ingrese_name()#!
                imprimir_key_jugador(nombre)
            case 7:
                jugador_max_rebote = calcular_mostrar_maximo(lista_jugador,"estadisticas", "rebotes_totales")
                imprimir_data(jugador_max_rebote)
            case 8:
                jugador_max_porcentaje_tiros = calcular_mostrar_maximo(lista_jugador,"estadisticas","porcentaje_tiros_de_campo" )
                imprimir_data(jugador_max_porcentaje_tiros)
            case 9:
                mayor_cantidad_asistencias_totales = calcular_mostrar_maximo(lista_jugador,"estadisticas","asistencias_totales" )
                imprimir_data(mayor_cantidad_asistencias_totales)
            case 10:
                solicitar_mostrar_maximo_segun_clave(lista_jugador,"promedio_puntos_por_partido")
            case 11:
                solicitar_mostrar_maximo_segun_clave(lista_jugador,"promedio_rebotes_por_partido")
            case 12:
                solicitar_mostrar_maximo_segun_clave(lista_jugador,"promedio_asistencias_por_partido")
            case 13:
                robos_totales_max = calcular_mostrar_maximo(lista_jugador,"estadisticas","robos_totales" )
                imprimir_data(robos_totales_max)
            case 14:
                bloqueos_totales_max = calcular_mostrar_maximo(lista_jugador,"estadisticas","bloqueos_totales" )
                imprimir_data(bloqueos_totales_max)
            case 15:
                solicitar_mostrar_maximo_segun_clave(lista_jugador, "porcentaje_tiros_libres")
            case 16:
                calcular_mostrar_clave_segun_jugador()
            case 17:
                maxima_cantidad_logros(lista_jugador)
            case 18:
                solicitar_mostrar_maximo_segun_clave(lista_jugador,"porcentaje_tiros_triples")
            case 19:
                solicitar_mostrar_maximo_segun_clave(lista_jugador,"temporadas")
            case 20:
                ordenados_posicion_cancha(lista_jugador)
            case 21:
                break #exit
            case 23:
                break #bonus
        clear_console()

menu()
