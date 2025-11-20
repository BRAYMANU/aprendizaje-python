# ==========================================
# Taller 1: Entrada - Salida de datos en Python
# Autor: [Brayan Manuel Erazo Estrada]
# ==========================================

"""
en python para trbajar la interaccion entre el usario y el programa 
utilizamos:
    Variales: Espacio en memoria donde guardamos datos
    Entrada de datos: Funcion input()
    salida de datos: fFuncion print()
"""

# pedimos datos al usuario
nombre = input("Dijite su nombre: ")
edad = int(input("Dijite su edad: "))
estatura = float(input("Dijite su estatura: "))
Telefono = int(input("Dijite su numero de celular: "))


# mostramos un mensaje con los datos ingresados
print("\n Hola",nombre,", se ha registrado tu edad que es de",edad,"años, tu estatura que es de \n" 
"",estatura,"centimetros, y tu telefono que es",Telefono,".")

"""
aqui se aplica:
    .Entrada de datos (input())
    .conversion de tipo (int) para convertir la edad a numero.
    .conversion de tipo (float) para convertir la estatura a numero desimal.
    .conversion de tipo (int) para convertir el telefono a numero.
"""

#===============================
#Salida de datos con formato
#===============================

"""
En Python es posible mostrar información en pantalla de una manera organizada usando
salida de datos con formato.
Para esto se puede utilizar el operador de formateo %, también conocido como operador de interpolación.
Este operador permite insertar variables dentro de una cadena de texto, especificando
el tipo de dato que se desea mostrar.
Sintaxis general: print("cadena con formato" % (variables_separadas_por_comas)).
Además, se puede controlar la cantidad de decimales, por ejemplo: %.2f muestra solo 2 decimales.
"""
#%c = un caracter
titulo = "la suma"
valor = 2+2
print ("el resultado de %s es %f " % (titulo, valor))

#%s = str, cadena de caracteres
nombre = "Manuel Erazo"
print("Hola, mi nombre es %s" % (nombre))

#%d = int, enteros
edad = 25
print("Tengo %d años" % (edad))

#%f = float, flotantes
pi = 3.14159265
print("El valor de pi con 2 decimales es: %.2f" % (pi)) #salida con dos decimales


#===================
#Imprseion de cadenas 
#===================

"""podemos mostrar cadenas de varias formas por pantalla"""

frase1 = "manuel"
frase2 = "quiere aprender a"
frase3 = "manejar python"

# el signo (+) los usamos para cocatenacion de cadenas 
print(frase1+" "+frase2+" "+frase3)

# el signo (*) me permite repiter cadenas 
print(frase1*3)

#con el metodo (capitalize()) podemos dar salida una palabra inicializada con mayuscula
print(frase1.capitalize())

#con el metodo (lower()) pasamos todo a minusculas
print(frase1.lower())

#con el metodo (upper()) pasamos todo a mayuscula
print(frase2.upper())

#con el metodo (title()) convertimos cada letra inicial a mayuscula
print(frase3.title())

