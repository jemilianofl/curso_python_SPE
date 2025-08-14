#==================================================================== 
# MÓDULO 6: LIBRERÍAS EXTERNAS Y APLICACIONES EN MACHINE LEARNING 
# ====================================================================
# -------------------------------------------------------------------- 
# 1 NUMPY Y PANDAS: LA BASE DEL ANÁLISIS DE DATOS
# -------------------------------------------------------------------- 
# NumPy (Numerical Python)
# NumPy es la librería fundamental para la computación numérica en Python. 
# Proporciona un objeto array que es mucho más rápido y flexible que las listas 
# de Python para realizar operaciones matemáticas.

import numpy as np
import time
import matplotlib.pyplot as plt

# Crear un array en NumPy
datos_pozo = np.array([150.0, 155.5, 160.2, 158.0, 165.7])
print(f"Array de datos: {datos_pozo}")
print(type(datos_pozo))
print(type([150.0, 155.5, 160.2, 158.0, 165.7]))

def suma_matrices_vanilla(matriz_a, matriz_b):
    """Suma dos matrices usando listas de Python."""
    filas = len(matriz_a)
    cols = len(matriz_a[0])
    
    matriz_resultado = [[0 for _ in range(cols)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(cols):
            matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]
            
    return matriz_resultado

def suma_matrices_numpy(matriz_a, matriz_b):
    """Suma dos matrices usando NumPy."""
    return matriz_a + matriz_b

# Definimos el tamaño de la matriz
tamano = 50000

print(f"Creando matrices de {tamano}x{tamano}...")

# Creamos matrices aleatorias para la prueba en formato vanilla
matriz_a_vanilla = [[i * j for j in range(tamano)] for i in range(tamano)]
matriz_b_vanilla = [[i + j for j in range(tamano)] for i in range(tamano)]

# Creamos matrices equivalentes en formato NumPy
matriz_a_np = np.array(matriz_a_vanilla)
matriz_b_np = np.array(matriz_b_vanilla)

# --- Medimos el tiempo con Python Vanilla ---
print("\n--- Suma con Python Vanilla ---")
inicio_vanilla = time.time()
suma_matrices_vanilla(matriz_a_vanilla, matriz_b_vanilla)
fin_vanilla = time.time()
tiempo_vanilla_grande = fin_vanilla - inicio_vanilla
print(f"Tiempo de ejecución: {tiempo_vanilla_grande:.4f} segundos")


# --- Medimos el tiempo con NumPy ---
print("\n--- Suma con NumPy ---")
inicio_numpy = time.time()
suma_matrices_numpy(matriz_a_np, matriz_b_np)
fin_numpy = time.time()
tiempo_numpy_grande = fin_numpy - inicio_numpy
print(f"Tiempo de ejecución: {tiempo_numpy_grande:.4f} segundos")

print(f"\nNumPy fue aproximadamente {tiempo_vanilla_grande / tiempo_numpy_grande:.0f} veces más rápido para este tamaño de matriz.")

# --- Visualización de los resultados ---
plt.figure(figsize=(8, 6))
tiempos = [tiempo_vanilla_grande, tiempo_numpy_grande]
etiquetas = ['Python Vanilla', 'NumPy']

plt.bar(etiquetas, tiempos, color=['skyblue', 'lightgreen'])
plt.title('Comparación de Tiempo de Suma de Matrices')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.show()


