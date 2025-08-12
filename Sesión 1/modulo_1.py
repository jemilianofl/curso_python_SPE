# ==================================================================== 
# MODULO 1: INTRODUCCIÓN Y FUNDAMENTOS DE DATOS 
# ==================================================================== 
# -------------------------------------------------------------------- 
# 1. PYTHON: TIPADO DINÁMICO PERO FUERTE 
# -------------------------------------------------------------------- 
# Python infiere el tipo de dato de una variable (dinámico). Sin embargo, 
# no permite operaciones entre tipos incompatibles sin una conversión explícita 
# (fuerte), lo que ayuda a prevenir errores. 

# Ejemplo de tipado dinámico: 
profundidad = 150.5 # Python sabe que es un float

nombre_pozo = "Pozo_A1" # Python sabe que es un string 

# Ejemplo de tipado fuerte (intenta descomentar la línea de abajo para ver el error): 

# print(5 + " metros")

print(str(5) + " metros") # La conversión explícita permite la operación. 

# -------------------------------------------------------------------- 
# 2. TIPOS DE DATOS BÁSICOS 
# -------------------------------------------------------------------- 
# Los bloques de construcción para almacenar información. 

# int: números enteros (e.g., 42) 
# float: números decimales (e.g., 3.14) 
# str: texto (e.g., "geología") 
# bool: valores lógicos (True/False)

temperatura = 35.8 # float 
print(type(temperatura))

nombre_pozo = "Pozo_A1" # str
print(type(nombre_pozo))

es_pozo = True # bool
print(type(es_pozo))

nombre_pozo = 'P' # str
print(type(nombre_pozo))

edad = 4500000000000000 # int
temperatura = 35.8 # float 
tipo_roca = "Sedimentaria" # str 
es_explorable = True # bool 
print("\n--- Tipos de datos básicos ---") 
print(f"La edad de la roca es: {edad} años. Tipo: {type(edad)}") 
print(f"La temperatura es: {temperatura}°C. Tipo: {type(temperatura)}") 

# -------------------------------------------------------------------- 
# 3. OPERADORES 
# -------------------------------------------------------------------- 
# Son símbolos que realizan operaciones sobre valores y variables. 
# --- Operadores Aritméticos --- 
# +, -, *, /, ** (exponenciación), % (módulo, el residuo de una división), // (división entera) 
print(5 % 2)
print(5 // 2)
print(5 / 2)
print(1 / 3)

profundidad_inicial = 100.0 # en metros 
profundidad_final = 150.0 # en metros 
tiempo_perforacion = 5.0 # en horas 
tasa_perforacion = (profundidad_final - profundidad_inicial) / tiempo_perforacion 
print(f"La tasa de perforación es: {tasa_perforacion} m/h.") 

# -- Operadores de comparación
# Estos operadores devuelven un valor booleano (True o False) y son la base de las 
# estructuras de control de flujo (if, while).
# ==, !=, >, <, >=, <=
# Ejemplo de operadores de comparación 
a = 10 
b = 20 
print(f"¿a es igual a b? {a == b}") 
print(f"¿a es menor que b? {a < b}") 
print(f"¿b es mayor o igual que a? {b >= a}")


# -- Operadores de Bit (Bitwise)
# Estos operadores actúan directamente sobre la representación binaria de los 
# números. Son menos comunes para tareas generales, pero esenciales en ciertos 
# campos como la criptografía, la computación científica o el desarrollo de drivers. 
# & AND, | OR, ^ XOR, ~ NOT, << Desplazamiento a la izquierda, >> Desplazamiento a la derecha
# Ejemplo de operadores de bit 
num1 = 5 # binario: 0101 
num2 = 3 # binario: 0011 
# AND: Los bits solo son 1 si ambos bits correspondientes son 1 
resultado_and = num1 & num2 # 0001 (1) 
print(f"5 & 3 = {resultado_and}") 
# OR: Los bits son 1 si al menos uno de los bits correspondientes es 1 
resultado_or = num1 | num2 # 0111 (7) 
print(f"5 | 3 = {resultado_or}") 
# Desplazamiento a la izquierda: desplaza los bits, multiplicando por potencias de 2
desplazamiento = num1 << 1 # 1010 (10) print(f"5 << 1 = {desplazamiento}")

# --- Operadores Lógicos --- 
# and, or, not 
# Usados para tomar decisiones en base a múltiples condiciones. 
porosidad_critica = 0.12 # 12% 
permeabilidad_critica = 25.0 # mD 
porosidad_muestra = 0.15 
permeabilidad_muestra = 30.5 
potencial_reservorio = (porosidad_muestra > porosidad_critica) and (permeabilidad_muestra > permeabilidad_critica) 
print(f"¿La muestra tiene potencial como reservorio? {potencial_reservorio}") 
temperatura_critica = 150.0 # °C 
temperatura_actual = 145.0 
# Usamos 'or' para verificar si al menos una condición es verdadera 
hay_riesgo = (temperatura_actual > temperatura_critica) or (permeabilidad_muestra > permeabilidad_critica) 
print(f"¿Hay algún riesgo operacional? {hay_riesgo}") 
# Usamos 'not' para negar una condición 
profundidad_final = 100 # en metros
es_somero = not (profundidad_final > 1000)
print(f"¿Es un pozo somero? {es_somero}")

# -------------------------------------------------------------------- 
# 4. ESTRUCTURAS DE DATOS DE PYTHON 
# -------------------------------------------------------------------- 
# Colecciones para almacenar múltiples datos de manera organizada. 

# --- Listas: Ordenadas, Mutables, Permiten duplicados --- 
# Ideales para colecciones de datos que necesitan cambiar. 
print("\n--- Listas ---") 
temperaturas = [25.5, 26.1, 27.8, 29.3, 27.8] 

print(f"Este es el primer elemento de la lista: {temperaturas[0]}")
print(f"Este es el ultimo elemento de la lista: {temperaturas[-1]}") # Slicing para obtener un subarray = [ x ) 0 <= x < 1
print(f"Lista de temperaturas: {temperaturas}") 
lista1 = [1, "Samantha", True, 4.6, 5]
print(f"Lista mixta: {lista1}")
# Métodos clave para listas: 
temperaturas.append(31.0) 
# .append(valor): añade un elemento al final. 
print(f"Después de append: {temperaturas}") 
temperaturas.insert(0, 24.0) 
# .insert(índice, valor): inserta un elemento en una posición específica. print(f"Después de insert: {temperaturas}") 
temperaturas.remove(27.8) 
# .remove(valor): elimina la primera ocurrencia del valor. 
print(f"Después de remove: {temperaturas}") 
temperaturas.pop(2)
# .pop(índice): elimina y retorna el elemento en el índice dado. 
print(f"Después de pop: {temperaturas}") 
temperaturas.sort(reverse=True)
# .sort(): ordena la lista en su lugar (ascendente por defecto). 
print(f"Después de sort: {temperaturas}") 
temperaturas.reverse() 
# .reverse(): invierte el orden de la lista. 
print(f"Después de reverse: {temperaturas}") 

print(f"Esto es una matriz: {[[1, 2, 3], [4, 5, 6]]}")

# --- Tuplas: Ordenadas, Inmutables, Permiten duplicados --- 
# Ideales para colecciones de datos fijos, como coordenadas. 
print("\n--- Tuplas ---") 
coordenadas = (123.456, -78.912, 123.456) 
# coordenadas[0]= 140
print(f"Coordenadas del pozo: {coordenadas}") 
# Métodos clave para tuplas (limitados por su inmutabilidad): 
print(f"Número de veces que aparece 123.456: {coordenadas.count(123.456)}") 
# .count(valor) 
print(f"Índice del valor -78.912: {coordenadas.index(-78.912)}") 
# .index(valor) 

# --- Conjuntos (Sets): No ordenados, Mutables, No permiten duplicados --- 
# Útiles para operaciones matemáticas de conjuntos y para asegurar que los elementos son únicos. 
print("\n--- Conjuntos (Sets) ---") 
minerales = {"cuarzo", "feldespato", "mica", "cuarzo"} 
print(f"Minerales encontrados (sin duplicados): {minerales}") 
# Métodos clave para conjuntos: 
minerales.add("pirita") 
# .add(valor): añade un elemento al conjunto. 
print(f"Después de add: {minerales}") 
minerales_segundo_analisis = {"mica", "calcita", "pirita"} 
interseccion = minerales.intersection(minerales_segundo_analisis) 
# .intersection(otro_set) 
print(f"Minerales en ambos análisis: {interseccion}") 
union = minerales.union(minerales_segundo_analisis) 
# .union(otro_set) 
print(f"Minerales únicos de ambos análisis: {union}") 

# --- Diccionarios: No ordenados, Mutables, Pares clave-valor --- 
# La estructura ideal para datos que tienen una relación clave-valor. 
print("\n--- Diccionarios ---") 
propiedades_roca = { "tipo": "caliza", "porosidad": 0.15, "permeabilidad": 50 } 
""" propiedades_roca = { "densidad": 2.71, "porosidad": -0.05, "permeabilidad": 0.01 } """ 
print(f"Propiedades de la roca: {propiedades_roca}") 
# Métodos clave para diccionarios: 
print(f"La porosidad de la roca es: {propiedades_roca.get('porosidad')}") 
# .get(clave) 
# .get() es más seguro que usar [] porque no da error si la clave no existe. propiedades_roca["color"] = "gris" 
# Añadir una nueva clave-valor. 
del propiedades_roca["permeabilidad"]
# del: elimina una clave y su valor. 
print(f"Después de eliminar permeabilidad: {propiedades_roca}") 
print(f"Todas las claves: {propiedades_roca.keys()}") 
print(f"Todos los valores: {propiedades_roca.values()}") 
print(f"Todos los pares: {propiedades_roca.items()}")

# JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos,

