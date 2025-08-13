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
import matplotlib.pyplot as plt
import random

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

def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        mitad_izquierda = lista[:mitad]
        mitad_derecha = lista[mitad:]
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)
        i = j = k = 0
        
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1
            
        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1
            
        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1

lista_desordenada = [64, 34, 25, 12, 22, 11, 90 , 1 , 3, 5, 20 , 6, 8, 9, 10, 87, 45, 78, 56, 23, 67]
inicio = time.time()
merge_sort(lista_desordenada)
print("Lista ordenada con Merge Sort:", lista_desordenada)
fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio} segundos")

tamanos_lista = [10, 100, 1000, 5000, 100000]

tiempos_lineal = []
tiempos_binaria = []
tiempos_bubble = []
tiempos_insertion = []
tiempos_merge = []

for n in tamanos_lista:
    lista_ordenada = list(range(n))
    lista_desordenada = list(range(n))
    random.shuffle(lista_desordenada)
    objetivo = -1 # El peor caso para los algoritmos de búsqueda

    # Medición de Búsqueda Lineal
    inicio = time.time()
    busqueda_lineal(lista_ordenada, objetivo)
    fin = time.time()
    tiempos_lineal.append(fin - inicio)

    # Medición de Búsqueda Binaria
    inicio = time.time()
    busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    tiempos_binaria.append(fin - inicio)

    # Medición de Bubble Sort y Insertion Sort (solo en listas pequeñas por su lentitud)
    if n <= 1000:
        lista_copia = lista_desordenada.copy()
        inicio = time.time()
        bubble_sort(lista_copia)
        fin = time.time()
        tiempos_bubble.append(fin - inicio)

        lista_copia = lista_desordenada.copy()
        inicio = time.time()
        insertion_sort(lista_copia)
        fin = time.time()
        tiempos_insertion.append(fin - inicio)
    else:
        tiempos_bubble.append(None)
        tiempos_insertion.append(None)
    
    # Medición de Merge Sort (es mucho más eficiente, lo podemos ejecutar en todas)
    lista_copia = lista_desordenada.copy()
    inicio = time.time()
    merge_sort(lista_copia)
    fin = time.time()
    tiempos_merge.append(fin - inicio)

plt.figure(figsize=(12, 8))

plt.plot(tamanos_lista, tiempos_lineal, label='Búsqueda Lineal O(n)', marker='o')
plt.plot(tamanos_lista, tiempos_binaria, label='Búsqueda Binaria O(log n)', marker='o')

tamanos_bubble_plot = [t for t, time in zip(tamanos_lista, tiempos_bubble) if time is not None]
tiempos_bubble_plot = [time for time in tiempos_bubble if time is not None]
plt.plot(tamanos_bubble_plot, tiempos_bubble_plot, label='Bubble Sort O(n^2)', marker='o')

tamanos_insertion_plot = [t for t, time in zip(tamanos_lista, tiempos_insertion) if time is not None]
tiempos_insertion_plot = [time for time in tiempos_insertion if time is not None]
plt.plot(tamanos_insertion_plot, tiempos_insertion_plot, label='Insertion Sort O(n^2)', marker='o')

plt.plot(tamanos_lista, tiempos_merge, label='Merge Sort O(n log n)', marker='o')

plt.title('Comparación de Complejidad de Algoritmos')
plt.xlabel('Tamaño de la lista (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()


