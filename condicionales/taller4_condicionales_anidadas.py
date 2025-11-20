#======================
#CONDICIONALES ANIDADAS
#======================

"""Una condicional anidada es cuando dentro de un if o else colocamos otro if.
esto nos permite evaluar varias condicones en diferentes niveles, como si fueran desiciones
dentro de otras decisiones.
    *Se llaman anidadas por que estan dentro de otra estructura condicional 
"""

#sintaxis
"""
if condicion1:
    # bloque si condicion1 es verdadera
    if condicion2:
        # bloque si condicion2 también es verdadera
    else:
        # bloque si condicion2 es falsa
else:
    # bloque si condicion1 es falsa
"""

#Ejemplo 1, Verificar edad y permiso
edad = 20
tiene_permiso = True

if edad >= 18:
    if tiene_permiso:
        print("Puede entrar")
    else:
        print("Necesitas un permiso especial")
else:
    print("Eres menor de edad")

#Ejemplo 2, Clasificacion de numeros
numero = -3

if numero >= 0:
    if numero == 0:
        print("El numero es cero")
    else:
        print("El numero es positivo")
else:
    print("El numero es negativo")

#Ejemplo 3, Sistema de notas
nota = 4.2

if nota >= 3:
    if nota >= 4.2:
        print("Excelente")
    else:
        print("Aprobado")
else:
    print("Reprobado")

#===============
#USO DE elif
#===============

"""En muchos casos no es necesario anidar if dentro de if.
Cuando tenemos multiles condiciones al mismo nivel, usamos elif (abreviatura de else if)
"""
#Sintaxis
"""
if condicion1:
    # bloque si condicion1 es verdadera
elif condicion2:
    # bloque si condicion2 es verdadera
elif condicion3:
    # bloque si condicion3 es verdadera
else:
    # bloque si ninguna condición es verdadera
"""
#Ejemplo 1: Clasificacion de notas
nota = 4.2

if nota < 3:
    print("Reprobado")
elif nota < 4.5:
    print("Aprobado")
else:
    print("Excelente")

#Ejemplo 2: Dias de la semana
dia = 3

if dia == 1: 
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
else:
    print("otro dia") 

#==================================
#EXPRESIONES BOOLEANAS COMPUESTAS
#==================================

"""Una expresion booleana compuesta combina varias condiciones usando operadores logicos(and, or, not).
esto permite resumir condiciones sin necesidad de anidar demasiado.
"""
#Ejemplo 1: Edad y permiso
edad = 18
permiso = True

if edad == 18 and permiso:
    print("Puedes ingresar")
else:
    print("No puedes ingresar")

#Ejemplo 2: Uso de or
dia = "sabado"
if dia == "sabado" or dia == "domingo":
    print("Es fin de semana")
else:
    print("Es dia laboral")


