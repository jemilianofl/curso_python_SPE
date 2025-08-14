# ==================================================================== 
# MÓDULO 5: ESTRUCTURAS DE DATOS AVANZADAS Y APLICACIONES 
# ====================================================================
# -------------------------------------------------------------------- 
# 1. Pilas (Stacks) LIFO
# -------------------------------------------------------------------- 
# Una pila es una colección de elementos que sigue el principio LIFO (Last-In, First-Out). 
# Imagina una pila de libros: el último libro que pones es el primero que quitas. Las pilas 
# se usan comúnmente para el historial de "deshacer" o la gestión de llamadas a funciones en 
# la memoria (el stack de llamadas).

class Pila:
    def __init__(self):
        self._items = []  # El uso de '_' indica que es una lista interna
        
    def esta_vacia(self):
        return not self._items
    
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        if not self.esta_vacia():
            return self._items.pop()
        return None  # Retorna None si la pila está vacía
    
    def ver_cima(self):
        if not self.esta_vacia():
            return self._items[-1]
        return None

# Ejemplo de uso de la pila
historial_acciones = Pila()
historial_acciones.push("Abrir archivo")
historial_acciones.push("Escribir código")
historial_acciones.push("Guardar")

print(f"La última acción fue: {historial_acciones.ver_cima()}")
historial_acciones.pop() # Elimina "Guardar"
print(f"La siguiente acción a deshacer es: {historial_acciones.ver_cima()}")

# -------------------------------------------------------------------- 
# 2. Colas (Queues): FIFO
# -------------------------------------------------------------------- 

# Una cola es una colección de elementos que sigue el principio FIFO (First-In, First-Out). 
# Piensa en la fila del supermercado: la primera persona que llega es la primera que es atendida. 
# Las colas se usan para procesar tareas en orden, como una fila de impresión o una lista de trabajos en un sistema operativo.

class Cola:
    def __init__(self):
        self._items = []

    def esta_vacia(self):
        return not self._items

    def encolar(self, item):
        self._items.insert(0, item) # Agregar al principio de la lista

    def desencolar(self):
        if not self.esta_vacia():
            return self._items.pop() # Eliminar del final de la lista
        return None

    def ver_frente(self):
        if not self.esta_vacia():
            return self._items[-1]
        return None

# Ejemplo de uso de la cola
cola_impresion = Cola()
cola_impresion.encolar("Documento_1.pdf")
cola_impresion.encolar("Informe_final.docx")
cola_impresion.encolar("Grafico.png")

print(f"El primer documento a imprimir es: {cola_impresion.ver_frente()}")
cola_impresion.desencolar() # Imprime "Documento_1.pdf"
print(f"El siguiente documento a imprimir es: {cola_impresion.ver_frente()}")

# -------------------------------------------------------------------- 
# 3. Árboles: Estructuras Jerárquicas no Lineales
# -------------------------------------------------------------------- 
# Los árboles son estructuras de datos no lineales y jerárquicas. Cada elemento, 
# llamado nodo, tiene un valor y puede estar conectado a otros nodos hijos. Los 
# árboles son fundamentales en la informática, ya que se usan en la organización 
# de sistemas de archivos, bases de datos y algoritmos de búsqueda.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  # Referencia al hijo izquierdo
        self.derecha = None    # Referencia al hijo derecho

# Clase para representar un Árbol Binario de Búsqueda (un tipo de árbol)
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None  # La raíz del árbol, el nodo principal

    def insertar(self, valor):
        # Lógica para insertar un nuevo nodo
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        
        nodo_actual = self.raiz
        while True:
            if valor < nodo_actual.valor:
                if nodo_actual.izquierda is None:
                    nodo_actual.izquierda = nuevo_nodo
                    return
                nodo_actual = nodo_actual.izquierda
            else:
                if nodo_actual.derecha is None:
                    nodo_actual.derecha = nuevo_nodo
                    return
                nodo_actual = nodo_actual.derecha

# Ejemplo de uso del árbol
arbol = ArbolBinarioBusqueda()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)

# Para visualizar el árbol, se necesita un método de recorrido
# (por ejemplo, In-order, Pre-order, Post-order).
# Aquí solo mostramos el valor de la raíz para simplificar.
print(f"\nLa raíz del árbol es: {arbol.raiz.valor}")
print(f"El nodo hijo izquierdo de la raíz es: {arbol.raiz.izquierda.valor}")
