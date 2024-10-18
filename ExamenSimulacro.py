import os

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def crear_array_bidimensional(filas, columnas):
    array = [[0 for _ in range(columnas)] for _ in range(filas)]
    return array

def mostrar_array(array):
    print("\nCalificaciones:")
    print(f"{'Bailarín':<15}{'Jurado 1':<10}{'Jurado 2':<10}{'Jurado 3':<10}{'Promedio':<10}")
    print("=" * 65)
    
    for i, fila in enumerate(array, start=1):
        promedio = calcular_promedio(fila)
        print(f"Bailarín     {fila[0]:<10}{fila[1]:<10}{fila[2]:<10}{promedio:<10.2f}")

def limpiar_consola() -> None:
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    option = int(input(mensaje))
    while option > maximo or option < minimo :    
        option = int(input(mensaje_error))
    return option

def ingresar_calificaciones(array):
    for i in range(len(array)): 
        for j in range(len(array[i])):
            array[i][j] = int(input(f"Ingrese la calificación del jurado {j + 1} para el Bailarín {i + 1}: "))


def ordenar_bailarines_por_jurado_2(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j][1] > array[j + 1][1]:  
                array[j], array[j + 1] = array[j + 1], array[j]


def encontrar_triple_siete(array):
    encontrado = False

    for i in range(len(array)):
        todas_siete = True  
        for j in range(len(array[i])): 
            if array[i][j] != 7:
                todas_siete = False
                break  

        if todas_siete:
            print(f"Bailarín {i + 1} tiene un 7 en todos los jurados.")
            encontrado = True 
    if not encontrado:
        print("No existen bailarines con calificación de 7 en todos los jurados.")

def mostrar_bailarines_aplazados(array):
    encontrado = False
    for i in range(len(array)):
        if array[i][2] < 4:  
            print(f"Bailarín {i + 1} fue aplazado por el jurado 3 con una nota de {array[i][2]}.")
            encontrado = True  
    if not encontrado:
        print("No existen bailarines aplazados por el jurado 3.")


def mostrar_top_3(array):
    promedios = [[0, 0] for _ in range(len(array))]
    for i in range(len(array)):
        promedio = calcular_promedio(array[i]) 
        promedios[i][0] = promedio  
        promedios[i][1] = i + 1  

    for i in range(len(promedios)):
        for j in range(len(promedios) - 1):
            if promedios[j][0] < promedios[j + 1][0]:  

                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
    print("\nTop 3 participantes con mayor nota promedio:")
    for i in range(min(3, len(promedios))):  
        print(f"Bailarín {promedios[i][1]}: Promedio = {promedios[i][0]:.2f}")


def obtener_nota_jurado1(ganador):
    return ganador[2]

def verificar_ganador(array):
    max_promedio = -1  
    ganadores = [] 

    for i in range(len(array)):
        promedio = calcular_promedio(array[i])
        
        if promedio > max_promedio:
            max_promedio = promedio
            ganadores = [[i + 1, promedio, array[i][0]]]  
        elif promedio == max_promedio:
            ganadores += [[i + 1, promedio, array[i][0]]]  

    if len(ganadores) > 1:
        max_jurado1 = obtener_nota_jurado1(ganadores[0]) 
        for ganador in ganadores:
            if obtener_nota_jurado1(ganador) > max_jurado1:
                max_jurado1 = obtener_nota_jurado1(ganador)
        ganadores_nuevos = []  
        for ganador in ganadores:
            if obtener_nota_jurado1(ganador) == max_jurado1:
                ganadores_nuevos += [ganador]  
        ganadores = ganadores_nuevos  

    print("\nGanadores de la competencia:")
    if len(ganadores) == 0:
        print("No hay ganadores.")
    else:
        for ganador in ganadores:
            print(f"Bailarín {ganador[0]}: Promedio = {ganador[1]:.2f}, Nota Jurado 1 = {ganador[2]}")


def ejecutar_menu():
    cargar_bailarines = 10
    cantidad_jurados = 3
    
    while(True):
        print("Competencia Bailarines\n1.Calificar Bailarines\n2.Mostrar Notas\n3.Ordenar Bailarines jurado 2\n4.Triple 7\n5.Jurado malo\n6.TOP 3\n7.Verificar Ganador\n8.Salir")
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-8\nSu opcion:",1,8)
        
        if opcion == 1:
            calificaciones = crear_array_bidimensional(cargar_bailarines, cantidad_jurados)
            ingresar_calificaciones(calificaciones)
        elif opcion == 2:
            mostrar_array(calificaciones)
        elif opcion == 3:
            ordenar_bailarines_por_jurado_2(calificaciones)
        elif opcion == 4:
            encontrar_triple_siete(calificaciones)
        elif opcion == 5:
            mostrar_bailarines_aplazados(calificaciones)
        elif opcion == 6:
            mostrar_top_3(calificaciones)
        elif opcion == 7:
            verificar_ganador(calificaciones)
        elif opcion == 8:
            break    
        limpiar_consola()
ejecutar_menu()