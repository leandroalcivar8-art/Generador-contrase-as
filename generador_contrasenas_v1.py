"""
Generador de Contraseñas
-------------------------
Programa que permite al usuario generar contraseñas seguras
personalizando su longitud y los tipos de caracteres incluidos.
 
Materia: Lógica de Programación
"""
 
import random
import string
 
 
def pedir_longitud():
    """
    Pide al usuario la longitud deseada para la contraseña.
    Usa un bucle para validar que el valor ingresado sea un
    número entero positivo dentro de un rango razonable.
    """
    while True:
        entrada = input("¿Cuántos caracteres tendrá la contraseña? (mínimo 4, máximo 64): ")
        if entrada.isdigit():
            longitud = int(entrada)
            # Estructura condicional para validar el rango permitido
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
    Si el usuario no elige ningún tipo, se le vuelve a preguntar
    (bucle de validación).
    """
    while True:
        print("\n¿Qué tipos de caracteres quieres incluir? (responde s/n)")
        usar_mayusculas = input("  Mayúsculas (A-Z): ").strip().lower() == "s"
        usar_minusculas = input("  Minúsculas (a-z): ").strip().lower() == "s"
        usar_numeros = input("  Números (0-9): ").strip().lower() == "s"
        usar_simbolos = input("  Símbolos (!@#$%...): ").strip().lower() == "s"
 
        # Condicional: al menos un tipo debe estar seleccionado
        if usar_mayusculas or usar_minusculas or usar_numeros or usar_simbolos:
            return {
                "mayusculas": usar_mayusculas,
                "minusculas": usar_minusculas,
                "numeros": usar_numeros,
                "simbolos": usar_simbolos,
            }
        else:
            print("\nDebes seleccionar al menos un tipo de carácter. Intenta de nuevo.")
 
 
def construir_set_caracteres(tipos):
    """
    A partir del diccionario de tipos seleccionados, arma el
    conjunto de caracteres disponibles para generar la contraseña.
    """
    caracteres_disponibles = ""
 
    if tipos["mayusculas"]:
        caracteres_disponibles += string.ascii_uppercase
    if tipos["minusculas"]:
        caracteres_disponibles += string.ascii_lowercase
    if tipos["numeros"]:
        caracteres_disponibles += string.digits
    if tipos["simbolos"]:
        caracteres_disponibles += "!@#$%&*?-_+="
 
    return caracteres_disponibles
 
 
def generar_contrasena(longitud, caracteres_disponibles):
    """
    Genera la contraseña carácter por carácter usando un bucle,
    eligiendo un carácter aleatorio del conjunto disponible
    en cada iteración.
    """
    contrasena = ""
 
    # Bucle repetitivo: agrega un carácter aleatorio en cada vuelta
    # hasta alcanzar la longitud solicitada
    for _ in range(longitud):
        caracter = random.choice(caracteres_disponibles)
        contrasena += caracter
 
    return contrasena
 
 
def evaluar_fortaleza(contrasena, tipos):
    """
    Evalúa qué tan fuerte es la contraseña generada según:
    - su longitud
    - la cantidad de tipos de caracteres distintos que usa
    Devuelve un texto: Débil, Media o Fuerte.
    """
    tipos_usados = sum(tipos.values())  # cuántos tipos están en True
    longitud = len(contrasena)
 
    # Estructura condicional anidada para clasificar la fortaleza
    if longitud >= 12 and tipos_usados >= 3:
        return "Fuerte"
    elif longitud >= 8 and tipos_usados >= 2:
        return "Media"
    else:
        return "Débil"
 
 
def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n========== GENERADOR DE CONTRASEÑAS ==========")
    print("1. Generar una contraseña")
    print("2. Salir")
    return input("Elige una opción (1/2): ").strip()
 
 
def main():
    """Función principal: controla el flujo del programa."""
    print("Bienvenido al Generador de Contraseñas")
 
    # Bucle principal del programa: se repite hasta que el usuario elija salir
    while True:
        opcion = mostrar_menu()
 
        # Condicional principal según la opción elegida
        if opcion == "1":
            longitud = pedir_longitud()
            tipos = pedir_tipos()
            caracteres_disponibles = construir_set_caracteres(tipos)
 
            contrasena = generar_contrasena(longitud, caracteres_disponibles)
            fortaleza = evaluar_fortaleza(contrasena, tipos)
 
            print("\n--- Resultado ---")
            print(f"Contraseña generada: {contrasena}")
            print(f"Fortaleza: {fortaleza}")
 
        elif opcion == "2":
            print("\nGracias por usar el Generador de Contraseñas. ¡Hasta luego!")
            break  # Termina el bucle principal y finaliza el programa
 
        else:
            print("\nOpción no válida. Por favor elige 1 o 2.")
 
 
# Punto de entrada del programa
if __name__ == "__main__":
    main()
