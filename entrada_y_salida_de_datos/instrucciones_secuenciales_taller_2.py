# ==========================================
# Taller 2: Instrucciones Secuenciales
# Autor: [Brayan Manuel Erazo Estrada]
# ==========================================

"""
Las instrucciones secuenciales son aquellas que se ejecutan una tras otra, 
en el mismo orden en que están escritas, sin tomar decisiones ni repetir pasos. 
  -Ejemplo: progama secuencial para registrar notas de un estudiante
"""
nombre = input("Ingrese el nombre del estudiante:") #entrada de texto
edad = int(input("Dijite la edad del estudiente:")) #entrada de numero entero
nota = float(input("Dijite la nota del estudiente:")) #entrada de numero flotante

print("\n====INFORMACION DEL ESTUDIANTE====")
print("Nombre:",nombre,"\n" \
"con edad de",edad,"años,\n" \
"nota final de:",nota)

#========================
#OPERADORES ARITMETICOS
#========================
"""
En las instrucciones secuenciales, es común realizar operaciones matemáticas básicas.
Python incorpora operadores que nos permiten trabajar con números de manera sencilla.
Si tomamos los valores a = 7 y b = 3 los principales operadores funcionan de la 
siguuiente manera:
"""
a,b = 7,3
print("Suma:", a + b)           # 10, suma
print("Resta:", a - b)          # 4, resta
print("Multiplicación:", a * b) # 21, multiplica
print("División:", a / b)       # 2.33333335, divide
print("Módulo:", a % b)         # 1, devuelve el residuo de dividr a entre b
print("Potencia:", a ** b)      # 343, potencia a elevado a la potencia b
print("División entera:", a // b)  # 2, devuelve la parte entera del cociente

#===========================
#INISIALISACION DE VARIABLES
#===========================
"""
Cuando se asigna por primera ves un valor a una variable, decidimos que se inicializa.
en python no se necesita declarar el tipo de la variable (entero, flotante, etc.), ya que
el interprete lo determina automaticamente segun lo que se asigne.
Ejemplos:
"""
a = 200      #variable inicializada con un numero entero
b = b ** 3   #variable inicializada con una expresion mateamtica 

#si nosotros intentamos usar una variable sin inicializar, python genera un error
#print(z)# Error: la variable no está definida

"""
CONSTANTES: En python una constante es un valor que no deberia cambiar a lo largo del programa
Por convención, se escriben en mayúsculas, aunque en realidad Python no impide modificar su valor.
Ejemplos:
"""
IVA = 0.19
precio_inicial = 3000
precio_final = precio_inicial * (1 + IVA)
print(precio_final)   # 3570

#una variable si puede cambiar de valor a lo largo del programa, asi:
a = 10000
print("Valor inicial de a:", a)

a = a + 200  # Aquí sí se modifica el valor de 'a'
print("Nuevo valor de a:", a)

"""
Python nos permite inisializar varias variables al mismo tiempo, asi:
"""
a = b = c = 10   # Todas con el mismo valor
print(a, b, c)   # 10 10 10

a, b, c = 100, 200, 300   # Cada una con un valor distinto
print(a, b, c)            # 100 200 300

"""
En programacion es comun usar Acumuladores y Contadores, asi:
"""
#Acumulador: variable a la que se le van sumando valores
suma = 0
edad = 20
suma = suma + edad   # suma = 20

#Contador: Variable que aumenta o disminuye en una cantidad constante 
total = 0
total = total + 1    # total = 1


#======================================================
#FUNCIONES PREDEFINIDAS O FUNCIONES INTERNAS EN PYTHON
#======================================================
"""
Python incluye muchas funciones internas que permiten realizar tareas comunes
sin necesidad de importar librerías.
Algunas de las más usadas son:
  print(): muestra datos en pantalla.
  input(): permite ingresar datos por teclado.
  len(): devuelve la longitud de una cadena o lista.
  type(): indica el tipo de dato de una variable.
  round(): redondea un número decimal.
  max() / min(): obtiene el mayor o menor de un conjunto.
"""
#Ejemplo:
nombre = input("Ingrese su nombre: ")
print("la longitud de la palbra",nombre,"es: ",len(nombre),"letras")

#=======================================
#LIBERRIA DE FECHA RANDOM Y MATEMATICAS
#=======================================
"""
Sirve para trabajar con fechas y horas.
Ejemplo:
"""
from datetime import date, datetime
print("Hoy es:", date.today()) #fecha actual
print("Fecha y hora actual:", datetime.now()) #hora y fecha actual

#=====================================
#NUMEROS ALEATORIOS (MODULO RANDOM)
#=====================================
"""Permite generar numeros o seleccionar elemntos al azar"""
import random
print(random.randint(10, 100))  # Entero aleatorio entre 10 y 100
print(random.random())          # Decimal aleatorio entre 0.0 y 1.0
print(random.choice(['Ana','Luis'])) # Selecciona un nombre al azar

#=====================================
#FUNCIONES MATEAMTICAS (MODULO MATH)
#=====================================
"""Incluye funciones avanzadas como raices, factoriales y trogonometria"""
import math
import math

print(math.sqrt(9))        # Raíz cuadrada → 3.0
print(math.factorial(5))   # Factorial → 120
print(math.fabs(-12.5))    # Valor absoluto → 12.5

ang = math.radians(60)     # Conversión a radianes
print(math.sin(ang))       # Seno de 60° → 0.866