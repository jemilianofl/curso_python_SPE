from mi_funcion import mi_funcion
# ==================================================================== 
# MODULO 2: PROGRAMACION FUNCIONAL Y DINAMICA 
# ==================================================================== # -------------------------------------------------------------------- 
# 1. FUNCIONES: ENCAPSULACION DE LOGICA
# -------------------------------------------------------------------- 
# Las funciones son bloques de código reutilizables. Nos permiten organizar el 
# código, hacerlo más legible y evitar la repetición. Piensa en una función como una 
# máquina que toma una entrada (parámetros), realiza un proceso y te devuelve una 
# salida (valor de retorno).

# Camel case
# miFuncion

# Snake case
# mi_funcion

print(mi_funcion(5, 10))  # Llamada a la función con argumentos 5 y 10

mi_variable = mi_funcion(3, 7)  # Guardamos el resultado de la función en una variable
print(mi_variable)  # Imprimimos el resultado almacenado en la variable

def fahrenheit_a_celsius(fahrenheit):
    """ Convierte una temperatura de grados Fahrenheit a Celsius. 
    Argumentos: 
    fahrenheit (float): Temperatura en grados Fahrenheit. 
    """ 
    
    celsius = (fahrenheit - 32) * (5/9)
    
    return celsius

# Usamos la función con un dato de ejemplo 
temperatura_en_f = 68.0
temperatura_en_c = fahrenheit_a_celsius(temperatura_en_f) 
print(f"La temperatura en Fahrenheit es: {temperatura_en_c}°F") 

# -------------------------------------------------------------------- 
# 2. FUNCIONES LAMBDA: FUNCIONES ANÓNIMAS Y SIMPLES
# -------------------------------------------------------------------- 
# Las funciones lambda son pequeñas funciones anónimas que puedes crear en una 
# sola línea. Son útiles para operaciones sencillas que no necesitas definir 
# formalmente con def. La sintaxis es lambda argumentos: expresión.

# Escenario: Tienes una lista de temperaturas en Fahrenheit y quieres convertirlas 
# todas a Celsius de forma rápida.

# Lista de temperaturas en grados Fahrenheit 
temperaturas_f = [32, 68, 86, 104] 

# Usamos una función lambda para definir la conversión en una sola línea 
conversor_celsius = lambda fahrenheit: (fahrenheit - 32) * 5/9

# Usamos la función lambda en un bucle para convertir cada temperatura 
temperaturas_c = [] 
for temp_f in temperaturas_f: temperaturas_c.append(conversor_celsius(temp_f)) 
print("\n--- Conversión con función lambda ---") 
print(f"Temperaturas en Fahrenheit: {temperaturas_f}") 
print(f"Temperaturas en Celsius: {temperaturas_c}")

# -------------------------------------------------------------------- 
# 3. FLUJO DE CONTROL IF/ELIF/ELSE
# -------------------------------------------------------------------- 
# Las estructuras de control de flujo son esenciales para que tu programa tome 
# decisiones. Te permiten ejecutar diferentes bloques de código basándose en si una
# condición es verdadera o falsa
# Escenario: Clasificar la calificación de un estudiante en un examen.

calificacion = 65

if calificacion >= 90:
    print("¡Excelente! Has obtenido una A.")
elif calificacion >= 80: 
    print("Muy bien, has obtenido una B.") 
elif calificacion >= 70: 
    print("Bien, has obtenido una C.")
else: 
    print("Necesitas mejorar, has obtenido una D o F.")

# Switch case

# -------------------------------------------------------------------- 
# 4. BUCLES: AUTOMATIZANDO TAREAS REPETITIVAS
# -------------------------------------------------------------------- 
# Los bucles son el motor de la automatización. Te permiten ejecutar un bloque de 
# código repetidamente, lo que es vital para procesar conjuntos de datos o realizar 
# simulaciones.

# Escenario: Imprimir cada nombre de una lista de estudiantes.
nombres = ["Ana", "Luis", "Carlos", "Marta"] 

# Bucle FOR para recorrer la lista de nombres 
print("--- Lista de Nombres ---") 
for nombre in nombres:
    print(f"Nombre: {nombre}")

# Ejemplo de WHILE: Conteo regresivo 
print("\n--- Conteo Regresivo ---")
contador = 5 
while contador > 0:
    print(contador)
    contador -= 1
print("¡Despegue!")

# -------------------------------------------------------------------- 
# 5. HACIA ALGORITMOS FUNCIONALES
# -------------------------------------------------------------------- 
# Combinar funciones, control de flujo y bucles es la clave para crear algoritmos.

# Escenario: Quieres escribir un algoritmo que busque si un nombre específico existe # en una lista.
estudiantes = ["Ana", "Luis", "Carlos", "Marta"] 
nombre_a_buscar = "Ana"

def buscar_nombre(lista, nombre):
    """ 
    Busca un nombre en una lista y devuelve True si lo encuentra, False en caso contrario. 
    """
    for item in lista: 
        if item == nombre: 
            return True # Retorna True y sale de la función 
        else: 
            return False # Retorna False si el bucle termina

if buscar_nombre(estudiantes, nombre_a_buscar): 
    print(f"\n{nombre_a_buscar} se encuentra en la lista.")
else: 
    print(f"\n{nombre_a_buscar} no se encuentra en la lista.")


