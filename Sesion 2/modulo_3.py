#  ==================================================================== 
# MÓDULO 3: ALGORITMOS, EFICIENCIA Y NOTACIÓN BIG O 
# ====================================================================
# -------------------------------------------------------------------- 
# 1. INTRODUCCIÓN A LA EFICIENCIA ALGORÍTMICA Y BIG O
# -------------------------------------------------------------------- 
# La notación Big O (O) es una forma de describir la eficiencia de un algoritmo, 
# específicamente su complejidad de tiempo. No mide el tiempo exacto en 
# segundos, sino cómo el tiempo de ejecución (o el número de operaciones) crece a 
# medida que el tamaño de la entrada, n, se hace más grande. Esto nos permite 
# predecir el comportamiento de un algoritmo en el peor de los casos.
# O(n) - Lineal: La ejecución es directamente proporcional al tamaño de la lista. (ej. Buscar en una lista desordenada).
# O(nlogn) - Log-lineal: El tiempo es más rápido que el cuadrático, muy # eficiente para listas grandes. (ej. Merge Sort).
# O(n^2) - Cuadrático: El tiempo de ejecución es proporcional al cuadrado del tamaño de la lista. (ej. Bubble Sort).
# O(log n) - Logarítmico: El tiempo de ejecución crece muy lentamente. Cada paso divide el problema por la mitad. (ej. Búsqueda binaria).

# -------------------------------------------------------------------- 
# 2. ALGORITMOS DE BÚSQUEDA Y SUS COMPLEJIDADES
# -------------------------------------------------------------------- 
# La búsqueda es la base de cualquier sistema que necesite encontrar datos. La 
# elección del algoritmo depende de si los datos están ordenados o no.

# Búsqueda Lineal (O(n))
# Este algoritmo recorre una lista elemento por elemento hasta que encuentra el valor 
# objetivo. Es simple de implementar y funciona en cualquier lista, pero es el más 
# lento en el peor de los casos (cuando el elemento no está o está al final).
import time

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna el índice si se encuentra
    return -1  # Retorna -1 si no se encuentra
lista_desordenada = [4, 2, 7, 1, 3, 5, 20 , 6, 8, 9, 10]
objetivo = 3
resultado = busqueda_lineal(lista_desordenada, objetivo)
print(f"Resultado de búsqueda lineal: {resultado}")

# Búsqueda Binaria (O(logn))
# Este algoritmo es mucho más rápido, pero solo funciona en listas ordenadas. El 
# algoritmo divide repetidamente la lista a la mitad y descarta la parte que no 
# contiene el valor.
def busqueda_binaria(lista, objetivo):
    bajo, alto = 0, len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio  # Retorna el índice si se encuentra
        elif lista[medio] < objetivo:
            bajo = medio + 1 
        else:
            alto = medio - 1
    return -1  # Retorna -1 si no se encuentra
inicio = time.time()
lista_ordenada = sorted(lista_desordenada)
resultado = busqueda_binaria(lista_ordenada, objetivo)
fin = time.time()
print(f"Resultado de búsqueda binaria: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio} segundos")

# -------------------------------------------------------------------- 
# 3. ALGORITMOS DE ORDENAMIENTO Y SUS COMPLEJIDADES
# -------------------------------------------------------------------- 
# El ordenamiento de datos es una operación fundamental que hace que la búsqueda y otras operaciones sean más eficientes.
# Bubble Sort (O(n2))
# Algoritmo didáctico, pero muy ineficiente. Compara y cambia elementos adyacentes si están en el orden incorrecto.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]  # Intercambia los elementos

lista_desordenada = [64, 34, 25, 12, 22, 11, 90 , 1 , 3, 5, 20 , 6, 8, 9, 10, 87, 45, 78, 56, 23, 67]
inicio = time.time()
bubble_sort(lista_desordenada)
print("Lista ordenada con Bubble Sort:", lista_desordenada)
fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio} segundos")

def bubble_sort_descendente(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

lista_desordenada = [64, 34, 25, 12, 22, 11, 90 , 1 , 3, 5, 20 , 6, 8, 9, 10, 87, 45, 78, 56, 23, 67]
inicio = time.time()
lista_ordenada_descendente = bubble_sort_descendente(lista_desordenada)
print("Lista ordenada de forma descendente:", lista_ordenada_descendente)
fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio} segundos")

# Insertion Sort (O(n2))
# También tiene una complejidad cuadrática, pero es más rápido que Bubble Sort en 
# listas pequeñas o casi ordenadas. Se construye la lista ordenada insertando un 
# elemento a la vez en su posición correcta.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        llave = lista[i]
        j = i - 1
        while j >= 0 and llave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = llave

lista_desordenada = [64, 34, 25, 12, 22, 11, 90 , 1 , 3, 5, 20 , 6, 8, 9, 10, 87, 45, 78, 56, 23, 67]
inicio = time.time()
insertion_sort(lista_desordenada)
print("Lista ordenada con Insertion Sort:", lista_desordenada)
fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio} segundos")

# Merge Sort (O(nlogn))
# Un algoritmo más avanzado y mucho más eficiente. Funciona con el principio de 
# "divide y vencerás": divide la lista en mitades, ordena cada una de ellas de forma 
# recursiva y luego las fusiona.

def mergf
