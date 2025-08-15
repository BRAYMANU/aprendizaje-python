# 02_tipos_datos.py

# ===========================
# TIPOS DE DATOS EN PYTHON
# ===========================

# --------------------
# 1. TIPOS BÁSICOS
# --------------------

# Enteros (int)  → Números sin parte decimal
numero_entero = 42
print("Número", numero_entero, type(numero_entero))

# Flotantes (float) → Números con parte decimal
numero_flotante = 3.14
print("Número", numero_flotante, type(numero_flotante))

# Cadena de texto (str) (str) → Texto entre comillas
texto = "hola, python"
print("Cadena:", texto, type(texto)) 

# Booleanos (bool) → True o False
es_verdadero = True
print("Booleano:", es_verdadero, type(es_verdadero))

# --------------------
# 2. TIPOS COMPUESTOS
# --------------------

# Listas (list) → Colección ordenada y modificable
lista = [1,2,3, "cuatro"]
print("Lista:", lista, type(lista))

# Tuplas (tuple) → Colección ordenada, pero inmutable
tupla = (1, 2, 3)
print("Tupla:", tupla, type(tupla))

# Conjuntos (set) → Colección no ordenada, sin elementos duplicados
conjunto = {1, 2, 3, 3}
print("Conjunto:", conjunto, type(conjunto))

# Diccionarios (dict) → Colección de pares clave-valor
diccionario = {"nombre": "manuel", "edad":25}
print("Diccionario:", diccionario, type(diccionario))

# --------------------
# 3. CONVERSIÓN ENTRE TIPOS
# -------------------- 

# En Python, puedes convertir valores de un tipo a otro usando funciones como int(), float(), str(), etc.
# Esto se conoce como "type casting".

# Convertir de entero a flotante
entero_a_flotante = float(10) # 10 -> 10.0
print("entero_a_flotante:", entero_a_flotante, type(entero_a_flotante))

# Convertir de flotante a entero (pierde la parte decimal)
flotante_a_entero = int(3.99) # 3.99 -> 3
print("flotante_a_entero:", flotante_a_entero, type(flotante_a_entero))

# Convertir de número a cadena de texto
número_a_texto = str(42) # 42 -> "42"
print("número_a_texto:", número_a_texto, type(número_a_texto))

# Convertir de texto a entero (el texto debe ser un número válido)
texto_a_entero = int("100")  # "100" -> 100
print("Texto a entero:", texto_a_entero, type(texto_a_entero))

# Convertir de texto a flotante
texto_a_flotante = float("3.14")  # "3.14" -> 3.14
print("Texto a flotante:", texto_a_flotante, type(texto_a_flotante))

# Lista a tupla
lista_a_tupla = tuple([1, 2, 3])
print("Lista a tupla:", lista_a_tupla, type(lista_a_tupla))

# Tupla a lista
tupla_a_lista = list((4, 5, 6))
print("Tupla a lista:", tupla_a_lista, type(tupla_a_lista))

# Lista a conjunto (elimina duplicados)
lista_a_conjunto = set([1, 2, 2, 3])
print("Lista a conjunto:", lista_a_conjunto, type(lista_a_conjunto))

# ==========================================
# 4. TIPOS DE DATOS AVANZADOS EN PYTHON
# ==========================================

# ------------------------------------------
# 1. Decimal (alta precisión en números)
# ------------------------------------------
# El tipo float puede dar resultados imprecisos debido a la forma en que
# representa los números en binario. Decimal evita estos errores.

from decimal import Decimal

decimal_preciso = Decimal("0.1") # Se pasa como string para evitar error inicial
print("Decimal preciso:", decimal_preciso, type(decimal_preciso))

# Ejemplo de precisión con Decimal
print("Suma con Decimal:", Decimal("0.1") + Decimal("0.2"))  # 0.3 exacto
print("Suma con Float:", 0.1 + 0.2) # 0.30000000000000004 (impreciso)

# ------------------------------------------
# 2. Fraction (fracciones exactas)
# ------------------------------------------
# Representa un número como fracción exacta (numerador/denominador).

from fractions import Fraction
fraccion = Fraction(1,3)
print("Fracción:", fraccion, type(fraccion))

# Ejemplo de operación con fracciones
resultado_fraccion = Fraction(1, 3) + Fraction(1, 6)  # 1/2 exacto
print("Suma de fracciones:", resultado_fraccion)


# ------------------------------------------
# 3. NoneType (valor nulo)
# ------------------------------------------
# None significa "sin valor" o "ausencia de valor".
valor_nulo = None
print("Valor nulo:", valor_nulo, type(valor_nulo))

# Ejemplo de uso común: verificar si una variable tiene valor asignado
respuesta = None
if respuesta is None:
    print("No hay respuesta todavía")








