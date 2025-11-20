# ==========================================
# Taller 3: Condicionales Simples
# Autor: [Brayan Manuel Erazo Estrada]
# ==========================================
#=======================
#CONDICIONALES SIMPLES
#=======================

"""En programacion los condicionales simples sirven para tomar desiciones dentro del codigo.
Si la condicion es verdadera(True), el flujo del programa continua en el bloque de instrucciones 
de la respuesta verdadera, de lo contrario el programa continua en el bloque de instrucciones 
de la respuesta falsa.
En python usamos la palabra clave (if) para indicar que una accion se ejecutara solo si se cumple una
condicion.

SINTAXIS BASICA:
    if condicion:
        # bloque de código que se ejecuta si la condición es verdadera.

.La condicion es una expresion que se evalua como verdadera(True) o falsa(False)
.Si la condision es verdadera, se ejecuta el bloque de codigo
.Si la condicion es falsa no se ejecuta.

"""

#=============
#USO DE IF:
#=============

#Ejemplo 1:
numero = 12
if numero > 0:
    print("El numero ingresado es positivo:",numero,"\n")
    print("El numero sera cambiado a: 5")
    numero = 5
    print("Ahora el numero ingresado es:",numero)

#Ejemplo 2: Comprobar si una persona es mayor de edad
edad = 18
if edad >= 18:
    print("Es mayor de edad")

#Ejemplo 3: Comparcion de cadenas
nombre = "Manuel"
if nombre == "Manuel":
    print("Hola, Manuel")

#==================
#USO DE IF ELSE
#==================
"""A veces necesitamos que, si la condicion no se cumple, El programa genere una 
accion alternatiiva.

SINTAXIS:
if condicion:
    # bloque que se ejecuta si la condición es verdadera
else:
    # bloque que se ejecuta si la condición es falsa
"""


#Ejemplo 1: Mayor o menor de edad
edad = int(input("Ingres su edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Ejemplo 2: numero positivo o negativo
numero = int(input("Ingrese un numero: "))
if numero >= 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

#Ejemplo 3: Verificacion de contraseña
password = input("Ingresa la contraseña: ")
if password == "manuel10":
    print("Contraseña Exitosa")
else:
    print("Contraseña Incorrecta")

#===================================
#OPERADORES COMUNES EN CONDICIONALES
#===================================
x = 5
#operador (==). (True) si el operando de la izquierda es igual al de la derecha; (False) en caso contrario
x == 5 #True

#operador (!=). (True) si el operador de la izquierda no es igual al de la derecha; (False) en caso contrario.
x != 5 #True

#operador (>). (True) si el operando de la derecha es estrictamente mayor que el operando de la izquierda; (False) en caso contrario.
x > 2 #True

#operador (<). (True) si el operando de la izquierda es estrictamente menor que el operando de la derecha; (False) en caso contrario. 
x < 10 #True

#operador (>=). (True) si el operador de la izquierda es mayor o igual que el de la derecha; (False) en caso contrario.
x >= 5 #True

#operador (<=). (True) si el operador de la izquierda es menor o igual que el de la derecha; (False) en caso contrario.
x <= 5 #True


#=====================
#OPERADORES BOOLEANOS
#=====================
"""Es importante conocer estos operadores ya que nos permiten negar o combinar condiciones dentro de un (if).
El resultado de una expresion booleana siempre es True(verdadero) o False(falso)."""

#and: Verdadero si ambas condiciones son verdaderas
#or: Verdadero si al menos una condicion es verdadera.
#not: invierte el valor de la condicion.

#jemplo 1; uso de (and)
edad = 20
if edad >= 18 and edad <= 30:
    print("Tienes entre 18 y 30 años.")

#ejmplo 2; uso de (or)
numero = 120
if numero == 0 or numero > 100:
    print("El número es válido")

#ejemplo 3; uso del (not)
password = input("Ingresa la contraseña: ")

if not password == "manuel10":
    print("Contraseña incorrecta")
