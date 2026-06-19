"""
Generador de Contraseñas
-------------------------
AVANCE INICIAL - Paso 1

Por ahora el programa:
- Muestra un menú
- Pide la longitud de la contraseña
- Pide qué tipos de caracteres incluir

Pendiente para el Paso 2:
- Generar la contraseña con los caracteres elegidos
- Calcular la fortaleza de la contraseña
- Manejar el ciclo completo de "generar otra"

Materia: Lógica de Programación
"""

import random
import string


def pedir_longitud():
    """
    Pide al usuario la longitud deseada para la contraseña.
    Valida que el valor ingresado sea un número entero positivo
    dentro de un rango razonable.
    """
    while True:
        entrada = input("¿Cuántos caracteres tendrá la contraseña? (mínimo 4, máximo 64): ")
        if entrada.isdigit():
            longitud = int(entrada)
            if 4 <= longitud <= 64:
                return longitud
            else:
                print("Error: la longitud debe estar entre 4 y 64. Intenta de nuevo.\n")
        else:
            print("Error: debes ingresar un número entero. Intenta de nuevo.\n")


def pedir_tipos():
    """
    Pregunta al usuario qué tipos de caracteres quiere incluir.
    Devuelve un diccionario con los tipos seleccionados (True/False).
    """
    while True:
        print("\n¿Qué tipos de caracteres quieres incluir? (responde s/n)")
        usar_mayusculas = input("  Mayúsculas (A-Z): ").strip().lower() == "s"
        usar_minusculas = input("  Minúsculas (a-z): ").strip().lower() == "s"
        usar_numeros = input("  Números (0-9): ").strip().lower() == "s"
        usar_simbolos = input("  Símbolos (!@#$%...): ").strip().lower() == "s"

        if usar_mayusculas or usar_minusculas or usar_numeros or usar_simbolos:
            return {
                "mayusculas": usar_mayusculas,
                "minusculas": usar_minusculas,
                "numeros": usar_numeros,
                "simbolos": usar_simbolos,
            }
        else:
            print("\nDebes seleccionar al menos un tipo de carácter. Intenta de nuevo.")


def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n========== GENERADOR DE CONTRASEÑAS ==========")
    print("1. Generar una contraseña")
    print("2. Salir")
    return input("Elige una opción (1/2): ").strip()


def main():
    """
    Función principal: por ahora solo recoge los datos del usuario.
    La generación real de la contraseña se implementará en el Paso 2.
    """
    print("Bienvenido al Generador de Contraseñas (versión en desarrollo)")

    opcion = mostrar_menu()

    if opcion == "1":
        longitud = pedir_longitud()
        tipos = pedir_tipos()

        # --- AVANCE ACTUAL ---
        print("\nDatos recolectados correctamente:")
        print(f"Longitud solicitada: {longitud}")
        print(f"Tipos seleccionados: {tipos}")
        print("\n(La generación de la contraseña se implementará en el siguiente avance)")

    elif opcion == "2":
        print("\nHasta luego.")

    else:
        print("\nOpción no válida.")


if __name__ == "__main__":
    main()
