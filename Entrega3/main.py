# ==============================================================================
# ENTREGA 3 - Práctica de Operador Ternario y *args
# Curso: Python Intermedio - Tecno3F
# Alumno: Matías Lorenzo
# ==============================================================================


# ------------------------------------------------------------------------------
# Ejercicio 1:
# Calcular el mayor de dos números ingresados por teclado usando un operador
# ternario.
# ------------------------------------------------------------------------------
def obtener_mayor(a, b):
    return a if a > b else b


def ejercicio_1():
    print("\n1. Mayor de dos números ingresados por teclado (Operador Ternario)")

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = (
            "Ambos números son iguales."
            if num1 == num2
            else f"El número mayor es: {obtener_mayor(num1, num2)}"
        )
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")


# ------------------------------------------------------------------------------
# Ejercicio 2:
# Buscar una palabra en una lista ingresada por teclado usando args y un operador
# ternario.
# ------------------------------------------------------------------------------
def buscar_palabra(palabra_buscada, *lista_palabras):
    encontrada = (
        f"La palabra '{palabra_buscada}' SÍ se encuentra en la lista."
        if any(palabra_buscada.lower() == palabra.lower() for palabra in lista_palabras)
        else f"La palabra '{palabra_buscada}' NO se encuentra en la lista."
    )
    return encontrada


def ejercicio_2():
    print("\n2. Buscar una palabra en una lista ingresada por teclado (*args y Ternario)")
    entrada_lista = input("Ingrese palabras separadas por espacios: ")
    palabras = [p.strip() for p in entrada_lista.split() if p.strip()]

    if not palabras:
        print("Aviso: No se ingresaron palabras en la lista.")
        return

    palabra_buscada = input("Ingrese la palabra que desea buscar: ").strip()
    if not palabra_buscada:
        print("Aviso: No ingresó una palabra válida para buscar.")
        return

    resultado = buscar_palabra(palabra_buscada, *palabras)
    print(f"Resultado: {resultado}")


# ------------------------------------------------------------------------------
# Ejercicio 3:
# Determinar si un número es par o impar.
# ------------------------------------------------------------------------------
def es_par_o_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar"


def ejercicio_3():
    print("\n3. Determinar si un número es par o impar (Operador Ternario)")
    try:
        numero = int(input("Ingrese un número entero: "))
        resultado = f"El número {numero} es {es_par_o_impar(numero)}."
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")


# ------------------------------------------------------------------------------
# Ejercicio 4:
# Calcular el promedio de una lista de números usando args y un operador ternario.
# ------------------------------------------------------------------------------
def calcular_promedio(*numeros):
    promedio = sum(numeros) / len(numeros) if len(numeros) > 0 else 0
    return promedio


def ejercicio_4():
    print("\n4. Calcular promedio de una lista de números (*args y Operador Ternario)")
    entrada = input("Ingrese números separados por espacios: ")
    try:
        numeros = [float(n) for n in entrada.split() if n.strip()]
        resultado = (
            f"El promedio de los números ingresados es: {calcular_promedio(*numeros):.2f}"
            if len(numeros) > 0
            else "No se ingresaron números para calcular el promedio."
        )
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Todos los elementos ingresados deben ser valores numéricos.")


# ------------------------------------------------------------------------------
# Ejercicio 5:
# Imprimir un mensaje de error si no se pasan suficientes argumentos.
# ------------------------------------------------------------------------------
def validar_argumentos_minimos(*args, minimo_requerido=2):
    mensaje = (
        f"Error: No se pasaron suficientes argumentos. Se requieren al menos {minimo_requerido} y se recibieron {len(args)}."
        if len(args) < minimo_requerido
        else f"Éxito: Se recibieron {len(args)} argumentos ({args}), cumpliendo el mínimo requerido de {minimo_requerido}."
    )
    print(mensaje)
    return len(args) >= minimo_requerido


def ejercicio_5():
    print("\n5. Imprimir mensaje de error si no se pasan suficientes argumentos (*args)")
    print("Demostración con función que requiere un mínimo de 2 argumentos:\n")

    print("[Prueba 1] Invocación sin argumentos:")
    validar_argumentos_minimos()

    print("\n[Prueba 2] Invocación con 1 solo argumento:")
    validar_argumentos_minimos("Elemento 1")

    print("\n[Prueba 3] Invocación con 3 argumentos:")
    validar_argumentos_minimos("Python", "Intermedio", "Tecno3F")


# ------------------------------------------------------------------------------
# Menú Principal Interactivo
# ------------------------------------------------------------------------------
def ejecutar_pruebas_automaticas():
    """Ejecuta una batería de pruebas demostrativas automáticas de todos los ejercicios."""
    print("\n" + "#" * 70)
    print("EJECUCIÓN DE PRUEBAS AUTOMÁTICAS")
    print("#" * 70)

    print("\n--- Ejercicio 1: Mayor de dos números ---")
    print(f"Mayor entre 15 y 42: {obtener_mayor(15, 42)}")
    print(f"Mayor entre 100 y 25: {obtener_mayor(100, 25)}")

    print("\n--- Ejercicio 2: Buscar palabra con *args ---")
    palabras_demo = ("python", "intermedio", "programacion", "tecno3f")
    print(f"Lista de prueba: {palabras_demo}")
    print(f"Buscando 'python': {buscar_palabra('python', *palabras_demo)}")
    print(f"Buscando 'java': {buscar_palabra('java', *palabras_demo)}")

    print("\n--- Ejercicio 3: Par o Impar ---")
    print(f"Número 14: {es_par_o_impar(14)}")
    print(f"Número 27: {es_par_o_impar(27)}")

    print("\n--- Ejercicio 4: Promedio con *args ---")
    print(f"Promedio de (8, 9, 10): {calcular_promedio(8, 9, 10):.2f}")
    print(f"Promedio de (4, 5, 6, 7): {calcular_promedio(4, 5, 6, 7):.2f}")
    print(f"Promedio sin argumentos (): {calcular_promedio():.2f}")

    print("\n--- Ejercicio 5: Validación de argumentos mínimos ---")
    validar_argumentos_minimos()
    validar_argumentos_minimos("Unico argumento")
    validar_argumentos_minimos("Arg 1", "Arg 2", "Arg 3")


def menu():
    while True:
        print("\n" + "=" * 70)
        print("  CURSO PYTHON INTERMEDIO - TECNO3F | ENTREGA 3")
        print("=" * 70)
        print("1. Ejercicio 1: Mayor de dos números (teclado + operador ternario)")
        print(
            "2. Ejercicio 2: Buscar palabra en lista (teclado + *args + operador ternario)")
        print("3. Ejercicio 3: Determinar si un número es par o impar (operador ternario)")
        print("4. Ejercicio 4: Calcular promedio de lista de números (*args + operador ternario)")
        print("5. Ejercicio 5: Validar cantidad suficiente de argumentos (*args)")
        print("0. Salir")
        print("=" * 70)

        opcion = input("Seleccione una opción (0-5): ").strip()

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "0":
            print("\nSaliendo...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 5.")


if __name__ == "__main__":
    menu()
