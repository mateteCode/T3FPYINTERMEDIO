# ==============================================================================
# ENTREGA 2 - Practica de Manejo de Excepciones
# Curso: Python Intermedio - Tecno3F
# Alumno: Matías Lorenzo
# ==============================================================================
import os

# ------------------------------------------------------------------------------
# Ejercicio 1:
# Escribe un programa que intente dividir dos números. Si el segundo número es
# cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al
# usuario.
# ------------------------------------------------------------------------------
print("1. División de dos números con captura de ZeroDivisionError:")


def dividir(a, b):
    try:
        resultado = a / b
        print(f"Resultado de {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError as e:
        print(f"Error: No se puede dividir por cero ({a} / {b}). Detalle: {e}")
        return None


# Casos de prueba
print("Caso exitoso:")
dividir(10, 2)

print("\nCaso con error (división por cero):")
dividir(10, 0)


# ------------------------------------------------------------------------------
# Ejercicio 2:
# Escribe un programa que intente sumar un número y una cadena. Si se produce
# un error de tipo, captura la excepción TypeError y muestra un mensaje de
# error al usuario.
# ------------------------------------------------------------------------------
print("\n2. Suma de un número y una cadena con captura de TypeError:")


def sumar_numero_y_cadena(a, b):
    try:
        resultado = a + b
        print(f"Resultado de {a} + {b} = {resultado}")
        return resultado
    except TypeError as e:
        print(
            f"Error de tipo (TypeError): No se puede sumar '{a}' ({type(a).__name__}) "
            f"con '{b}' ({type(b).__name__}). Detalle: {e}"
        )
        return None


# Caso de prueba
print("Caso con error (int + str):")
sumar_numero_y_cadena(10, "5")


# ------------------------------------------------------------------------------
# Ejercicio 3:
# Escribe un programa que intente acceder a una clave que no existe en un
# diccionario. Si se produce una excepción KeyError, captura la excepción y
# muestra un mensaje de error al usuario.
# ------------------------------------------------------------------------------
print("\n3. Acceso a clave de diccionario con captura de KeyError:")

estudiante = {
    "nombre": "Matias Lorenzo",
    "curso": "Python Intermedio"
}


def consultar_diccionario(diccionario, clave):
    try:
        valor = diccionario[clave]
        print(f"Clave '{clave}' encontrada -> Valor: {valor}")
        return valor
    except KeyError as e:
        print(
            f"Error de clave (KeyError): La clave {e} no existe en el diccionario.")
        return None


# Casos de prueba
print(f"Diccionario de prueba: {estudiante}\n")
print("Caso exitoso:")
consultar_diccionario(estudiante, "curso")

print("\nCaso con error (clave inexistente):")
consultar_diccionario(estudiante, "edad")


# ------------------------------------------------------------------------------
# Ejercicio 4:
# Escribe un programa que intente abrir un archivo que no existe. Si se produce
# una excepción FileNotFoundError, captura la excepción y muestra un mensaje
# de error al usuario. Sin embargo, también intenta crear el archivo si no existe.
# ------------------------------------------------------------------------------
print("\n4. Apertura y creación de archivo con captura de FileNotFoundError:")


def abrir_o_crear_archivo(ruta_archivo):
    try:
        print(f"Intentando abrir el archivo '{ruta_archivo}'...")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(
                f"Archivo abierto exitosamente. Contenido:\n{contenido.strip()}")
    except FileNotFoundError as e:
        print(f"Error (FileNotFoundError): El archivo no existe. Detalle: {e}")
        print(f"Creando el archivo '{ruta_archivo}'...")
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("Archivo de prueba.\n")
            print(f"Archivo '{ruta_archivo}' creado exitosamente.")
        except Exception as error_creacion:
            print(f"No se pudo crear el archivo: {error_creacion}")


# Si existe el archivo lo eliminamos para probar el error
directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_prueba = os.path.join(directorio_actual, "archivo_prueba.txt")
if os.path.exists(archivo_prueba):
    os.remove(archivo_prueba)

# Casos de prueba
print("Primera ejecución (archivo inexistente):")
abrir_o_crear_archivo(archivo_prueba)

print("\nSegunda ejecución (el archivo ya existe):")
abrir_o_crear_archivo(archivo_prueba)


# ------------------------------------------------------------------------------
# Ejercicio 5:
# Escribe un programa que intente dividir dos números. Si el segundo número es
# cero, captura la excepción ZeroDivisionError. Si el primer número es un
# número no válido, captura la excepción ValueError. En cualquier caso, muestra
# un mensaje de error al usuario.
# ------------------------------------------------------------------------------
print("\n5. División con validación de primer número (ValueError y ZeroDivisionError):")


def dividir_valores(primer_valor, segundo_valor):
    try:
        num1 = float(primer_valor)
        num2 = float(segundo_valor)
        resultado = num1 / num2
        print(f"Resultado de {num1} / {num2} = {resultado}")
        return resultado
    except ValueError as e:
        print(
            f"Error de valor (ValueError): El valor ingresado '{primer_valor}' no es un número válido. Detalle: {e}")
        return None
    except ZeroDivisionError as e:
        print(
            f"Error de división (ZeroDivisionError): No se puede dividir por cero ({num1} / {num2}). Detalle: {e}")
        return None


# Casos de prueba
print("Caso Exitoso:")
dividir_valores("20", 4)

print("\nCaso Error en el primer valor (ValueError):")
dividir_valores("abc", 5)

print("\nCaso División por cero (ZeroDivisionError):")
dividir_valores(15, 0)
