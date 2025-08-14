# ==================================================================== 
# MÓDULO 4: PROGRAMACIÓN ORIENTADA A OBJETOS (POO) 
# ====================================================================
# -------------------------------------------------------------------- 
# 1. CLASES Y OBJETOS
# -------------------------------------------------------------------- 
# - Clase: Piensa en una clase como un plano de construcción. Es una plantilla que 
# define las características (qué tiene) y los comportamientos (qué hace) de un 
# objeto. Una clase no es el objeto en sí, sino la receta para crearlo.
# - Objeto: Un objeto es una instancia de esa clase. Es la casa real construida a partir
# del plano. Puedes crear múltiples objetos a partir de la misma clase, y cada uno 
# tendrá sus propios valores para las características definidas en el plano.

# -------------------------------------------------------------------- 
# 2. MÉTODOS
# -------------------------------------------------------------------- 
# Los métodos son las funciones que pertenecen a un objeto. Se definen dentro de 
# una clase y permiten que el objeto haga algo.

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad  # Atributo de instancia

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        
estudiante1 = Estudiante("Juan", 20)
estudiante1.presentarse()  # Llama al método presentarse del objeto estudiante1

# -------------------------------------------------------------------- 
# 3. LOS 4 PILARES DE LA POO
# -------------------------------------------------------------------- 
# Estos principios son la base de la POO y se aplican para diseñar código más 
# escalable y fácil de mantener.

# 1. Encapsulación
# Es la práctica de agrupar los datos y los métodos que operan sobre ellos en una 
# única unidad (la clase). Esto oculta los detalles internos y protege los datos, 
# permitiendo que el objeto sea una "caja negra" con una interfaz clara.
class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, cantidad):
        self._saldo += cantidad
    
    def ver_saldo(self):
        return self._saldo

mi_cuenta = CuentaBancaria(100)
mi_cuenta.depositar(50)
print(f"Mi saldo actual es: {mi_cuenta.ver_saldo()}")

# 2. Abstracción
# Es el proceso de ocultar la complejidad y mostrar solo la funcionalidad necesaria. 
# Nos permite enfocarnos en qué hace el objeto, no en cómo lo hace. Por ejemplo, al 
# conducir un coche, la abstracción te permite usar el volante sin entender el 
# complejo mecanismo de la dirección.

# 3. Herencia
# Permite que una clase herede atributos y métodos de otra clase. Esto fomenta la 
# reutilización de código y establece una relación de "es un". Por ejemplo, un 
# EstudianteUniversitario "es un" Estudiante y, por lo tanto, hereda sus características.

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

class Empleado(Persona):
    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

# Un objeto Empleado puede usar el método de la clase padre
empleado1 = Empleado("Juan")
empleado1.saludar()
empleado1.trabajar()

# 4. Polimorfismo
# Significa "muchas formas". Permite que objetos de diferentes clases respondan al 
# mismo mensaje de diferentes maneras. Por ejemplo, un método hablar() podría 
# tener un comportamiento distinto en una clase Perro ("guau guau") que en una clase # Gato ("miau miau").

class Gato:
    def hablar(self):
        return "miau miau"

class Perro:
    def hablar(self):
        return "guau guau"

# Una función que puede manejar objetos de diferentes clases
def hacer_sonido(animal):
    print(animal.hablar())

mi_gato = Gato()
mi_perro = Perro()

hacer_sonido(mi_gato)
hacer_sonido(mi_perro)

# -------------------------------------------------------------------- 
# 4. PRINCIPIOS SOLID
# -------------------------------------------------------------------- 
# Ahora, apliquemos los principios SOLID para construir algoritmos de regresión.
# Esto demuestra la diferencia entre un script funcional y una solución de software 
# bien diseñada.

# 1. Principio de Responsabilidad Única (SRP)
# Una clase debe tener una sola razón para cambiar. Esto significa que una clase debe tener una única responsabilidad. 
# Si una clase tiene más de una, se vuelve frágil y difícil de mantener.
# La clase Estudiante solo tiene la responsabilidad de almacenar sus datos
class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

# La clase CalculadoraDeCalificaciones solo se encarga de la lógica de cálculo
class CalculadoraDeCalificaciones:
    def calcular_promedio(self, estudiante):
        return sum(estudiante.notas) / len(estudiante.notas)

estudiante1 = Estudiante("Ana", [85, 90, 78, 92])
calculadora = CalculadoraDeCalificaciones()
promedio = calculadora.calcular_promedio(estudiante1)
print(f"El promedio de {estudiante1.nombre} es: {promedio:.2f}")

# 2. Principio de Abierto/Cerrado (OCP)
# Una clase debe estar abierta para la extensión, pero cerrada para la modificación. 
# Debes poder añadir nuevas funcionalidades sin cambiar el código de las clases existentes. 
# La herencia es la herramienta clave para lograrlo.

# Clase base que define un contrato (Principio Abierto/Cerrado)
class Figura:
    def area(self):
        raise NotImplementedError

# La clase Cuadrado extiende a Figura, sin modificarla
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

# La clase Circulo también extiende a Figura
import math
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)

figuras = [Cuadrado(4), Circulo(5)]

print("\n--- Calculando áreas ---")
for figura in figuras:
    print(f"El área de la figura es: {figura.area():.2f}")

# 3. Principio de Sustitución de Liskov (LSP)
# Los objetos de una clase base deben poder ser sustituidos por objetos de sus subclases sin romper el programa. 
# Una clase hija debe tener un comportamiento compatible con el de la clase padre.

# Mismo código que el ejemplo anterior, demostrando el LSP.
# El bucle 'for' espera un objeto de tipo Figura, y los objetos
# Cuadrado y Circulo se pueden sustituir sin problemas.

def calcular_areas(lista_de_figuras):
    for figura in lista_de_figuras:
        print(f"El área es: {figura.area():.2f}")

figuras_a_calcular = [Cuadrado(3), Circulo(2)]
print("\n--- Demostración de Liskov ---")
calcular_areas(figuras_a_calcular)

# 4. Principio de Segregación de Interfaces (ISP)
# Es mejor tener muchas interfaces específicas que una sola interfaz grande y general. 
# En Python, esto se aplica a las clases base: una clase no debe ser forzada a implementar 
# métodos que no necesita.

# Clase base para animales que pueden volar
class PuedeVolar:
    def volar(self):
        raise NotImplementedError

# Clase base para animales que pueden nadar
class PuedeNadar:
    def nadar(self):
        raise NotImplementedError

# Un Pato hereda de ambas clases
class Pato(PuedeVolar, PuedeNadar):
    def volar(self):
        print("El pato está volando.")
    def nadar(self):
        print("El pato está nadando.")

# Un Pinguino solo hereda de PuedeNadar
class Pinguino(PuedeNadar):
    def nadar(self):
        print("El pinguino está nadando.")

print("\n--- Segregación de Interfaces ---")
pato = Pato()
pato.volar()
pato.nadar()

pinguino = Pinguino()
pinguino.nadar()

# 5. Principio de Inversión de Dependencia (DIP)
# Las clases de alto nivel no deben depender de las de bajo nivel. 
# Ambas deben depender de abstracciones. En lugar de que un módulo 
# dependa de los detalles de otro, ambos dependen de una abstracción (como una clase base).

# Abstracción: El lector de datos
class LectorDeDatos:
    def leer_datos(self):
        raise NotImplementedError

# Clase de bajo nivel: El lector concreto de CSV
class LectorDeCSV(LectorDeDatos):
    def leer_datos(self):
        return "Leyendo datos desde un archivo CSV..."

# Clase de alto nivel: El analizador, que depende de la abstracción
class AnalizadorDeDatos:
    def __init__(self, lector: LectorDeDatos):
        # El Analizador no sabe si es un CSV o un JSON, solo sabe que es un LectorDeDatos.
        self.lector = lector
    def analizar(self):
        datos = self.lector.leer_datos()
        print(f"Analizando: {datos}")

print("\n--- Inversión de Dependencia ---")
lector_csv = LectorDeCSV()
analizador = AnalizadorDeDatos(lector_csv)
analizador.analizar()
