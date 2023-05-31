#Pozo, Mariano Leonel , div H  
import re
import json
import os
import csv


def clear_console() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls' para borrar la pantalla.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

with open('C:\\Users\\Inoue\\Desktop\\carpet\\Programacion_I\\Parcial\\dt.json') as archivo:
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
    """
    Esta función calcula el promedio de un valor específico en una lista de diccionarios.
    
    :param jugadores: una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type jugadores: list
    :param primera_clave: La primera clave para acceder al diccionario dentro de la información de cada
    jugador
    :type primera_clave: str
    :param segunda_clave: La segunda clave o atributo del diccionario anidado dentro del diccionario de
    cada jugador que contiene el valor que se usará para calcular el promedio
    :type segunda_clave: str
    :return: un valor flotante, que es el promedio de un valor específico (determinado por la segunda
    clave) en una lista de diccionarios (determinado por la primera clave). Si la lista está vacía,
    devuelve Ninguno.
    """
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
    """
    Esta función calcula e imprime los puntos promedio por juego para una lista de jugadores y luego
    imprime los nombres de los jugadores y sus puntos promedio individuales por juego en orden
    alfabético.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas
    """


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
    """
    Esta función toma un diccionario que representa a un jugador de baloncesto, comprueba si es miembro
    del Salón de la Fama del Baloncesto e imprime un mensaje que indica si es miembro o no.
    
    :param jugador_encontrado: Un diccionario que contiene información sobre un jugador de baloncesto,
    incluido su nombre y logros
    :type jugador_encontrado: dict
    """
    
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
    """
    La función "imprimir_datos" imprime el parámetro de entrada.
    
    :param dato_a_impirimir: Esta es una variable que representa los datos que deben imprimirse. Puede
    ser cualquier tipo de datos, como una cadena, un número entero, un flotante o incluso una lista o un
    diccionario. La función "imprimir_datos" toma este parámetro y lo imprime en la consola
    """
    print(dato_a_impirimir)

#7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales. 
#8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo. %
#9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.

def calcular_mostrar_maximo(lista_jugadores: list[dict], clave_jugador:str, clave_valor:str)-> str:
    """
    Esta función toma una lista de diccionarios que contienen información del jugador, una clave para
    identificar al jugador y una clave para identificar un valor para cada jugador, y devuelve un
    mensaje que indica qué jugador tiene el valor más alto para la clave dada.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus atributos
    :type lista_jugadores: list[dict]
    :param clave_jugador: La clave en el diccionario para la información del jugador (por ejemplo,
    "nombre", "edad", "equipo")
    :type clave_jugador: str
    :param clave_valor: El parámetro "clave_valor" es una cadena que representa la clave de un valor en
    un diccionario que está asociado a un jugador en una lista de jugadores. Este valor se utiliza para
    determinar el valor máximo entre todos los jugadores de la lista
    :type clave_valor: str
    :return: un mensaje de cadena que indica el jugador con el valor más alto para una clave determinada
    en una lista de diccionarios de jugadores. Si la lista está vacía o hay un error, devuelve un
    mensaje de error.
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

#10) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
#más puntos por partido que ese valor.
#11) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
#más rebotes por partido que ese valor.
#12) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
#más asistencias por partido que ese valor.
#19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
def solicitar_mostrar_maximo_segun_clave(lista_jugadores:dict, clave: str):
    """
    Esta función solicita al usuario que ingrese un valor y luego busca en una lista de estadísticas de
    jugadores valores mayores que el valor de entrada para una tecla específica, e imprime el nombre del
    jugador y la estadística correspondiente.
    
    :param lista_jugadores: una lista de diccionarios que contienen información sobre los jugadores y
    sus estadísticas
    :param clave: El parámetro "clave" es una cadena que representa la clave o atributo de las
    estadísticas del jugador que la función usará para comparar con el valor ingresado por el usuario.
    Se normaliza reemplazando los guiones bajos con espacios para que sea más legible en el mensaje de
    salida
    """
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
    """
    Esta función encuentra al jugador con el mayor número de logros en una lista de jugadores.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y una lista de los logros que ha obtenido
    """
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
    """
    Esta función calcula el promedio de un valor específico en una lista de diccionarios.
    
    :param jugadores: una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type jugadores: list
    :param primera_clave: La primera tecla para acceder al diccionario de cada jugador de la lista
    :type primera_clave: str
    :param segunda_clave: La segunda clave o atributo del diccionario que está anidado dentro de la
    lista de jugadores
    :type segunda_clave: str
    :return: un valor flotante, que es el promedio de un valor específico (determinado por la segunda
    clave) en una lista de diccionarios (determinado por la primera clave). Si la lista está vacía,
    devuelve Ninguno.
    """
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
    La función ordena una lista de diccionarios por una clave doble, ya sea en orden ascendente o
    descendente.
    
    :param lista: Una lista de diccionarios que se ordenarán según los valores de sus claves
    :type lista: list
    :param primera_clave: La primera clave para ordenar la lista. Debe ser una cadena que represente el
    nombre de la clave en los diccionarios dentro de la lista
    :type primera_clave: str
    :param segunda_clave: El parámetro "segunda_clave" es una cadena que representa la segunda clave o
    atributo que se utilizará para ordenar la lista de diccionarios en la función
    "ordenar_por_clave_doble". Se usa en conjunto con el parámetro "primera_clave" para ordenar la lista
    de diccionarios
    :type segunda_clave: str
    :param flag_orden: Un indicador booleano que determina si la lista debe ordenarse en orden
    ascendente o descendente en función de los valores de las claves especificadas
    :type flag_orden: bool
    :return: La función `ordenar_por_clave_doble` devuelve una lista ordenada basada en dos claves
    (`primera_clave` y `segunda_clave`) y una bandera (`flag_orden`) que determina si la ordenación debe
    ser ascendente o descendente.
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
    """
    Esta función calcula y muestra el promedio de puntos por juego para una lista de jugadores,
    excluyendo al jugador con el promedio más bajo.
    """
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

#asd

def obtener_jugadores_con_estadisticas_ordenadas(lista_jugadores:list[dict])-> list[dict]:
    """
    Esta función toma una lista de diccionarios que representan a los jugadores de baloncesto y sus
    estadísticas, ordena a los jugadores por diferentes estadísticas y devuelve una nueva lista de
    diccionarios con los nombres de los jugadores y sus clasificaciones en cada estadística.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus estadísticas
    :type lista_jugadores: list[dict]
    :return: una lista de diccionarios con las estadísticas modificadas de los jugadores, donde cada
    diccionario contiene el nombre del jugador y sus estadísticas actualizadas para cada categoría
    (rebotes, asistencias, robos y puntos).
    """
    
    lista_copia = lista_jugadores[:]

    lista_estadisticas = ["rebotes_totales", "asistencias_totales", "robos_totales", "puntos_totales"]
    for estadistaca in lista_estadisticas:
        lista_ordenada = ordenar_por_clave_doble(lista_copia,"estadisticas" ,estadistaca , False)
        jugadores_con_estadisticas = []

        for i in range(len(lista_ordenada)):
            jugador = lista_ordenada[i]
            nombre = jugador["nombre"]
            jugador["estadisticas"][estadistaca] = i + 1
            jugador_modificado = {
                "nombre": nombre,
                "estadisticas": jugador["estadisticas"]
            }
            jugadores_con_estadisticas.append(jugador_modificado)


    return jugadores_con_estadisticas
def guardar_archivo_csv(nombre_archivo: str, contenido: str) -> bool:
    """
    Esta función guarda el contenido de una cadena en un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operación fue exitosa o no.

    Parametros: 
        -nombre_archivo: Una cadena que representa el nombre del archivo que se va a crear o
        sobrescribir

        -contenido: El contenido que se escribirá en el archivo. Debería ser una cadena

    :retorno: 
        -un valor booleano, ya sea True o False, según si el archivo se creó correctamente o no.
    """
 
    with open(nombre_archivo, 'w') as archivo:
        resultado = None 
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

def generar_texto(data:list[dict] or dict)->str:

    """
    La función genera una representación de texto de los datos del jugador de baloncesto en formato de
    lista o de diccionario.
    
    :param data: Los datos de entrada que pueden ser un diccionario o una lista de diccionarios que
    contienen información sobre los jugadores de baloncesto y sus estadísticas
    :return: La función `generar_texto` devuelve una cadena que contiene datos en un formato específico.
    El formato depende del tipo de `datos` de entrada. Si `data` es una lista de diccionarios, la
    función devuelve una cadena con valores separados por comas para cada diccionario de la lista. Si
    `data` es un diccionario, la función devuelve una cadena con valores separados por comas para las
    claves y valores en el diccionario
    """

    if isinstance(data, list):
        lista_claves = ["nombre", "asistencias totales", "puntos_totales", "rebotes_totales", "robos_totales"]
        filas = []

        for jugador in data:
            valores = [str(jugador["nombre"]),
                       str(jugador["estadisticas"]["asistencias_totales"]),
                       str(jugador["estadisticas"]["puntos_totales"]),
                       str(jugador["estadisticas"]["rebotes_totales"]),
                       str(jugador["estadisticas"]["robos_totales"])]
            fila = ",".join(valores)
            filas.append(fila)

        claves_str = ",".join(lista_claves)
        datos = "{0}\n{1}".format(claves_str, "\n".join(filas))

        return datos

    elif isinstance(data, dict):
        lista_claves = ["nombre", "posicion"]
        lista_valores = []

        jugador_estadisticas = data["estadisticas"]
        nombre_posicion = "{0}, {1}".format(data["nombre"], data["posicion"])

        for clave, valor in jugador_estadisticas.items():
            lista_claves.append(clave)
            lista_valores.append(str(valor))

        claves_str = ",".join(lista_claves)
        valores_str = ",".join(lista_valores)

        datos_str = "{0}\n{1},{2}".format(claves_str, nombre_posicion, valores_str)
        return datos_str

    else:
        return False

def imprimir_guarda_tabla_jugadores(lista_jugadores: list[dict])-> None:

    """
    Esta función imprime una tabla de estadísticas de jugadores y la guarda en un archivo CSV.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus estadísticas. Cada diccionario contiene las claves "nombre" y "estadisticas" que es otro
    diccionario que contiene las claves "puntos_totales" (total de puntos), "rebotes_totales" (total de
    rebotes), "
    :type lista_jugadores: list[dict]
    """

    print("---------------------------------------------------------------------------")
    print("|     Jugador          |    Puntos  |   Rebotes |  Asistencias  |  Robos  |")
    print("---------------------------------------------------------------------------")
    for jugador in lista_jugadores:
        print("|  {:19s} | {:^10d} | {:^9d} | {:^13d} | {:^7d} |".format(
            jugador["nombre"],
            jugador["estadisticas"]["puntos_totales"],
            jugador["estadisticas"]["rebotes_totales"],
            jugador["estadisticas"]["asistencias_totales"],
            jugador["estadisticas"]["robos_totales"])
        )
    print("---------------------------------------------------------------------------")


# asd1

def contar_posicion(lista_jugadores)-> None:
    """
    La función cuenta el número de jugadores en un equipo de baloncesto por su posición e imprime los
    resultados.
    
    :param lista_jugadores: una lista de diccionarios que representan a jugadores de baloncesto, donde
    cada diccionario contiene información sobre un jugador, como su nombre, edad, altura, peso y
    posición. La función cuenta el número de jugadores en cada categoría de posición e imprime los
    resultados
    """

    contador_escolta = 0
    contador_base = 0
    contador_ala_pivot = 0
    contador_alero = 0
    contador_pivot = 0 
    for jugador in lista_jugadores:
        if jugador["posicion"] == "Escolta":
            contador_escolta += 1
        elif jugador["posicion"] == "Base":
            contador_base += 1
        elif jugador["posicion"] == "Ala-Pivot":
            contador_ala_pivot += 1
        elif jugador["posicion"] == "Alero":
            contador_alero += 1
        elif jugador["posicion"] == "Pivot":
            contador_pivot += 1
    print("Escolta: {0}".format(contador_escolta))
    print("Base: {0}".format(contador_base))
    print("Ala-Pivot: {0}".format(contador_ala_pivot))
    print("Alero: {0}".format(contador_alero))
    print("Pivot: {0}".format(contador_pivot))

#26

def calcular_maximo(lista_jugadores:list, primera_clave:str):
    """
    Recibe una lista de diccionarios, y dos claves.
    Busca el valor máximo según las claves especificadas en la lista.
    Devuelve el diccionario del jugador máximo.
    """
    valor_maximo = 0
    jugador_maximo = None

    for jugador in lista_jugadores:
        valor = jugador["estadisticas"].get(primera_clave, 0)
        if valor > valor_maximo:
            valor_maximo = valor
            jugador_maximo = jugador

    return jugador_maximo

def maximo_segun_estadisticas(lista_jugadores:list) -> str:

    mensaje = ""
    for jugador in lista_jugadores:
        for clave in jugador["estadisticas"]:
            max_estadisticas = calcular_maximo(lista_jugadores, clave)
            nombre_max_estadisticas = max_estadisticas["nombre"]
            valor_max_estadisticas = max_estadisticas["estadisticas"][clave]
            mensaje += f"{clave}: {nombre_max_estadisticas} - {valor_max_estadisticas}\n"

        if clave == "porcentaje_tiros_triples":
            break

    return mensaje


#27 e 4


def encontrar_mejor_jugador_mejor_estadistica(lista_jugadores:list[dict])-> None:
    """
    Esta función encuentra al jugador con las mejores estadísticas generales de una lista de jugadores.

    :param lista_jugadores: una lista de diccionarios que representan a los jugadores y sus
    estadísticas. Cada diccionario debe tener las siguientes claves: "nombre" (nombre del jugador,
    cadena), "estadisticas" (estadísticas del jugador, diccionario con claves como nombres de
    estadísticas y valores como valores de estadísticas, int)
    :type lista_jugadores: list[dict]
    """

    if lista_jugadores:
        max_jugador = None
        max_puntaje = 0

        for jugador in lista_jugadores:
            estadistica_total = 0
            for estadistica in jugador["estadisticas"].values():
                estadistica_total += estadistica
                if max_jugador is None or estadistica_total > max_puntaje:
                    max_jugador = jugador
        print("jugador tiene las mejores estadísticas :{0} con la suma total de : {1}".format(max_jugador["nombre"] , estadistica_total))
    else:
        print("Error, lista vacia!")


'''def validar_opcion():
    opcion = input("ingrese opcion: ")'''
    

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
                # El código selecciona un jugador basado en un índice de una lista de jugadores, luego
                # guarda los datos del jugador seleccionado en un archivo CSV ubicado en
                # "Parcial\data.csv". La función utilizada para guardar los datos en el archivo no se
                # muestra en el fragmento de código.
                ruta_archivo = "Parcial\data.csv" # jugador_indice_estadistica.csv
                selec_indic = seleccionar_jugador_por_indice(lista_jugador)
                datos_para_guardar = selec_indic
                guardar_archivo(ruta_archivo, datos_para_guardar)
            case 4:
                # El código llama a una función "show_players" con un parámetro "player_list" y
                # almacena el valor devuelto en una variable "opción". Luego imprime el valor de
                # "opción" Luego llama a una función "login_name()" y almacena el valor devuelto en
                # una variable "names_to_choose". Finalmente, llama a una función "name_achievements"
                # con los parámetros "names_to_choose" y "player_list".
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
                jugadores_con_estadisticas = obtener_jugadores_con_estadisticas_ordenadas(lista_jugador)
                nombre_archivo = "estadisticas_jugadores.csv"
                texto_generado = generar_texto(jugadores_con_estadisticas)
                guardar_archivo_csv(nombre_archivo, texto_generado)
                imprimir_guarda_tabla_jugadores(jugadores_con_estadisticas)
            case 24:
                contar_posicion(lista_jugador)
            case 25:
                pass
            case 26:
                '''estadisticas = "estadisticas"
                claves = []
                mensaje = ""
                for estadistica in lista_jugador:
                    claves.append(estadistica[estadisticas])
                    for clave in len(range(claves)):
                        max_valor = calcular_mostrar_maximo(estadistica, "estadisticas", clave)
                        mensaje += solicitar_mostrar_maximo_segun_clave(max_valor, clave)

                return print(mensaje)     '''   

                '''max_temporadas = calcular_mostrar_maximo(lista_jugador, estadisticas, "temporadas")
                max_puntos_totales = calcular_mostrar_maximo(lista_jugador, estadisticas, "puntos_totales")
                max_promedio_puntos = calcular_mostrar_maximo(lista_jugador, estadisticas, "promedio_puntos_por_partido")
                max_rebotes_totales = calcular_mostrar_maximo(lista_jugador, estadisticas, "rebotes_totales")
                max_promedio_rebotes = calcular_mostrar_maximo(lista_jugador, estadisticas, "promedio_rebotes_por_partido")
                max_asistencias_totales = calcular_mostrar_maximo(lista_jugador, estadisticas, "asistencias_totales")
                max_promedio_asistencias = calcular_mostrar_maximo(lista_jugador, estadisticas, "promedio_asistencias_por_partido")
                max_robos_totales = calcular_mostrar_maximo(lista_jugador, estadisticas, "robos_totales")
                max_bloqueos_totales = calcular_mostrar_maximo(lista_jugador, estadisticas, "bloqueos_totales")
                max_porcentaje_tiros_campo = calcular_mostrar_maximo(lista_jugador, estadisticas, "porcentaje_tiros_de_campo")
                max_porcentaje_tiros_libres = calcular_mostrar_maximo(lista_jugador, estadisticas, "porcentaje_tiros_libres")
                max_porcentaje_tiros_triples = calcular_mostrar_maximo(lista_jugador, estadisticas, "porcentaje_tiros_triples")
                solicitar_mostrar_maximo_segun_clave(max_temporadas, "temporadas")
                solicitar_mostrar_maximo_segun_clave(max_porcentaje_tiros_campo, "porcentaje_tiros_de_campo")
                solicitar_mostrar_maximo_segun_clave(max_puntos_totales, "puntos_totales")
                solicitar_mostrar_maximo_segun_clave(max_promedio_puntos, "promedio_puntos_por_partido")
                solicitar_mostrar_maximo_segun_clave(max_rebotes_totales, "rebotes_totales")
                solicitar_mostrar_maximo_segun_clave(max_promedio_rebotes, "promedio_rebotes_por_partido")
                solicitar_mostrar_maximo_segun_clave(max_asistencias_totales, "asistencias_totales")
                solicitar_mostrar_maximo_segun_clave(max_promedio_asistencias, "promedio_asistencias_por_partido")
                solicitar_mostrar_maximo_segun_clave(max_robos_totales, "robos_totales")
                solicitar_mostrar_maximo_segun_clave(max_bloqueos_totales, "bloqueos_totales")
                solicitar_mostrar_maximo_segun_clave(max_porcentaje_tiros_campo, "porcentaje_tiros_de_campo")
                solicitar_mostrar_maximo_segun_clave(max_porcentaje_tiros_libres, "porcentaje_tiros_libres")
                solicitar_mostrar_maximo_segun_clave(max_porcentaje_tiros_triples, "porcentaje_tiros_triples")'''#corregir error str
            case 27:
                encontrar_mejor_jugador_mejor_estadistica(lista_jugador)
            case _:
                print( "Esa opcion no esta en el menu" )
                
        clear_console()

menu()
