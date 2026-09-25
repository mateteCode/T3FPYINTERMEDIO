# ==============================================================================
# ENTREGA 1 - Practica de Conjuntos (Sets)
# Curso: Python Intermedio - Tecno3F
# ==============================================================================

# Conjuntos de prueba
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {2, 3, 5}


# ------------------------------------------------------------------------------
# Ejercicio 1:
# Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
# elementos que se encuentran en A o en B, o en ambos.
# ------------------------------------------------------------------------------
print(f"\n1. Elementos en A {A} o en B {B}, o en ambos (Union):")
union = A | B
print(f"Resultado: {union}")


# ------------------------------------------------------------------------------
# Ejercicio 2:
# Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
# elementos que se encuentran en A y en B.
# ------------------------------------------------------------------------------
print(f"\n2. Elementos en A {A} y en B {B} (Interseccion):")
interseccion = A & B
print(f"Resultado: {interseccion}")


# ------------------------------------------------------------------------------
# Ejercicio 3:
# Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
# conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
# ------------------------------------------------------------------------------
print(
    f"\n3. Elementos en A {A} o en B {B}, pero no en ambos (Diferencia Simetrica):")
diferencia_simetrica = A ^ B
print(f"Resultado: {diferencia_simetrica}")


# ------------------------------------------------------------------------------
# Ejercicio 4:
# Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto
# es un subconjunto de otro conjunto, B.
# ------------------------------------------------------------------------------
print("\n4. Verificar si un conjunto es subconjunto de otro:")
print(
    f"El conjunto A {A} {'SI' if A.issubset(B) else 'NO'} es un subconjunto del conjunto B {B} ")
print(
    f"El conjunto C {C} {'SI' if C.issubset(A) else 'NO'} es un subconjunto del conjunto A {A} ")


# ------------------------------------------------------------------------------
# Ejercicio 5:
# Dados un conjunto, A, escribe un programa en Python que imprima el numero de
# elementos del conjunto.
# ------------------------------------------------------------------------------
print("\n5. Numero de elementos del conjunto:")
print(f"El conjunto A {A} tiene {len(A)} elementos.")
