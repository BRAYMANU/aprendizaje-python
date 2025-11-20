# ==========================================
# Taller 5: ciclo for en Python
# Autor: [Brayan Manuel Erazo Estrada]
# ==========================================

"""CICLO for: se usa en casos donde se sabe la cantidad de veces que se desesa ejecutar el bloque.
Se lo utiliza para iterar sobre una secuencia de elementos  (como listas, tuplas o cadenas de texto)
y ejecutar un bloque de codigo para cada elemento de esa secuencia.

SINTAXIS:
 for variable in iterable:
    codigo a ejecutar
    
-variable toma el valor de cada elemento en cada iteracion
-Iterable: Es la coleccion a recorrer(lista, Tupla, Conjunto, Dicciionario, cadena de texto).
 """
#Ejemplo 1:
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
print("fin del ciclo")

#=============
#USO DE RANGE
#=============
"""
range(inicio, fin, paso): Funcion que genera una secuencia de numeros.
    -Si solo se pone un numero empieza desde cero y llega hasta el numero que se coloco restado uno.
    -Si se coloca dos numeros empieza en el primero y llega hasta hasta el segundo numero -1.
    -si se pone tres; el tercero  define el incremento o decremento.
"""
#Ejemplo 1: Solo con un valor final
for i in range(5):
    print(i) #end=""
print("fin del ciclo")

#Ejemplo #2: Con valor inicial y final
for i in range(2,6):
    print(i, i**2, end="  ")
print("fin del ciclo")

# Ejemplo 3: Con inicio, fin y paso
for i in range(10, 0, -2):
    print(i)
print("fin del ciclo")

#=================================================
#CONCEPTOS: valor inicial, valor final, incremento
#=================================================
"""
    -Valor inicial: el numero donde comienza la secuencia.
    -Valor final: es el limite(este no se incluye).
    -Incremento: me indica cuanto aumenta o disminuye
"""
#Ejemplo 1: Incremento de uno
for i in range(1, 6):
    print(i)
print("fin del ciclo")

#Ejemplo 2: Incremento de 3
for i in range(0, 10, 3):
    print(i)
print("fin del ciclo")

#Ejemplo 3: Decremento
for i in range(20, 10, -2):
    print(i)
print("fin del ciclo")

#==================
#USOS Y ESTRUCTURA
#==================
"""
El ciclo for sirve para recorrer secuencias como (cadenas, listas, tuplas, conjuntos, diccionarios)
"""
#CADENAS
    #Ejemplo 1:
for letra in "manuel":
    print(letra)
print("fin del ciclo")

    #Ejemplo 2:
for palabra in "python":
    print(palabra)
print("fin del ciclo")

    #Ejemplo 2:
mensaje = "Iterar"
contador = 0
for c in mensaje:
    contador+=1
print(f"el numero de letras de la pabra {mensaje} es: {contador}")

#EN LISTAS
    #Ejemplo 1:
numeros = [1, 2, 3]
for n in numeros:
    print(n**2)
print("fin del ciclo")

    #Ejemplo 2:
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print("Me gusta la", fruta)
print("fin del ciclo")

    #Ejemplo 3:
edades = [15, 22, 30]
for edad in edades:
    print("Edad:", edad)
print("fin del ciclo")

#EN TUPLAS
    #Ejemplo 1:
datos = ("Alicia", 25, "Ingeniera")
for d in datos:
    print(d)
print("fin del ciclo")

    #Ejemplo 2:
coordenadas = (10, 20, 30)
for valor in coordenadas:
    print("Valor:", valor)
print("fin del ciclo")

    #Ejemplo 3:
login = ("usuario", "clave123")
for dato in login:
    print("Dato:", dato)
print("fin del ciclo")

#EN CONJUNTOS
    #Ejemplo 1:
A = {1, 2, 3, 4, 1}
for x in A:
    print(x)
print("fin del ciclo")

    #Ejemplo 2:
vocales = {"a", "e", "i", "o", "u"}
for v in vocales:
    print(v)
print("fin del ciclo")

    #Ejemplo 3:
colores = {"rojo", "verde", "azul, verde"}
for c in colores:
    print("Color:", c)
print("fin del ciclo")

#EN DICCIONARIOS
    #Ejemplo 1:
edades = {"Ana": 20, "Luis": 25}
for nombre, edad in edades.items():
    print(nombre, "tiene", edad, "años")
print("fin del ciclo")

    #Ejemplo 2:
precios = {"pan": 1000, "leche": 2500}
for producto in precios:
    print(producto, "vale", precios[producto])
print("fin del ciclo")

    #Ejemplo 3:
capitales = {"Colombia": "Bogotá", "Perú": "Lima"}
for pais, capital in capitales.items():
    print("La capital de", pais, "es", capital)

#==================================
#SENTENCIAS: break, continue y pass
#==================================

#break: Rompe el ciclo antes de terminar
    #Ejemplo 1
for i in range(10):
    if i == 5:
        break
    print(i)

    # Ejemplo 2
for letra in "Python":
    if letra == "h":
        break
    print(letra)

    # Ejemplo 3
for n in [1, 2, 3, 4, 5]:
    if n == 4:
        break
    print("Número:", n)

#continue: Salta a la siguiente iteracion
    #Ejemplo 1
for i in range(5):
    if i == 2:
        continue
    print(i)

    #Ejemplo 2
for letra in "Python":
    if letra == "o":
        continue
    print(letra)

    #Ejemplo 3
for n in [1, 2, 3, 4, 5]:
    if n % 2 == 0:
        continue
    print("Impar:", n)
    
#pass: no hace nada cuando se ejecuta
    #Ejemplo 1
for i in range(3):
    pass

    #Ejemplo 2
for letra in "ABC":
    if letra == "B":
        pass
    print("Letra:", letra)

    #Ejemplo 3
for n in range(5):
    if n == 2:
        pass
    print("Número:", n)

#=====================
#Estructura For- else
#=====================

#El bloque else se ejecutará cuando la expresión condicional del bucle for sea False..
    #Ejemplo 1
for i in range(3):
    print(i)
else:
    print("Ciclo terminado")

    #Ejemplo 2
for letra in "Hola":
    if letra == "o":
        break
    print(letra)
else:
    print("No se encontró 'x'")

    #Ejemplo 3
numeros = [2, 4, 6, 8]
for n in numeros:
    if n % 2 != 0:
        break
else:
    print("Todos son pares")

