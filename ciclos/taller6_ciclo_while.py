# ==========================================
# Taller 6: ciclo while en Python
# Autor: [Brayan Manuel Erazo Estrada]
# ==========================================

"""
Ciclo while: es una estructura de control iterativa que permite repetir un bloque de instrucciones 
mientras una condicion sea verdadera.
sintaxis:

while condicion:
    # Bloque de instrucciones

-Si la condicion es True se ejecuta el bloque.
-Si la condición es False, se termina el ciclo y el programa continúa con la siguiente instrucción.
"""

#====================
#Variables de control
#====================
"""
La condicion del ciclo suele depender de una variable de control. Esta deve inicializarse 
antes del ciclo while y modificarse dentro del while, para evitar un ciclo infinito.
"""
#Ejemplo 1: numeros del 1 al 5
i = 0
while i <= 5:
    print(i)
    i = i + 1
print("Fin del ciclo ")

# Uso de la operacion +=
i = 1
while i <= 10:
    print(i)
    i += 2  # Aumenta en 2 cada vez

#====================
#TIPO DE CICLOS while
#====================
"""
while controlado por contador: se repite un numero de veces, controlado por un contador o variable.
"""
# Ejemplo: 
total = 0
contador = 1

while contador <= 5:
    print("Valor:", contador)
    total += contador
    contador += 1
print("Total final: ", total)
print("Fin del ciclo while")

"""
while controlado por un evento: El ciclo depende de que ocurra un evento (por ejemplo: 
que el usuario escriba un valor)
"""
#Ejemplo:
print("=====Prgrama para registrar libros en una Bibiblioteca====")
total = 0
interfaz = input("Bienvenido a la interfaz de registrar libros ('1 para ingresar', '2 para salir'): ")

while interfaz == "1":
    nombre_libro = input("Ingresa el nombre del libro: ")
    tipo_libro = input("Ingrese el tipo de libro: ")
    codigo_libro = input("Ingrese el codigo del libro: ")
    total += 1
    interfaz = input("\nBienvenido a la interfaz de registrar libros ('1 para ingresar', '2 para salir'): ")
print("el numero de libros ingresados fue de:",total)


"""while con else: Se ejecuta cuando la condicion del while es false"""
#Ejemplo:
i = 1
while i <= 3:
    print("Iteracion", i)
    i +=1
else:
    print("Fin del ciclo (condicion falsa)")

#===============================
#SENTENCIAS DE CONTROL CON while
#===============================
"""
Break: Finaliza el ciclo antes de que la condicion sea falasa
"""
#Ejemplo
i = 10
while i > 0:
    print(i)
    if i == 5:
        break
    i-=1
print("Fin del ciclo")
    
"""
Coninue: omite el resto de instrucciones en esa iteracion y pasa a la siguiente
"""
i = 10
while i > 0:
    i -= 1
    if i == 3:
        continue
    print(i)
print("Fin del ciclo")

"""
Pass: Sirve como marcador de posición. No hace nada, pero evita errores de sintaxis.
"""
i = 3
while i >= 0:
    if i == 2:
        pass  # No hace nada
    print(i)
    i -= 1

#===============
# MAS EJEMPLOS
#===============
clave = ""
while clave != "manu123":
    clave = input("Ingrese la clave: ")
print("Acceso concedido")

import random
numero_secreto = random.randint(1, 10)
intento = 0
adivinado = False

while not adivinado:
    num = int(input("Adivina un número entre 1 y 10: "))
    intento += 1
    if num == numero_secreto:
        adivinado = True
        print("¡Correcto! Lo lograste en", intento, "intentos")
