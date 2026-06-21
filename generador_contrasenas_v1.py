"""
Generador de Contraseñas
-------------------------
Programa que permite al usuario generar contraseñas seguras
personalizando su longitud y los tipos de caracteres incluidos.
 
Incluye dos enfoques de generación:
1. Contraseña aleatoria (caracteres sueltos: mayúsculas, minúsculas,
   números, símbolos)
2. Passphrase (frase de palabras aleatorias, ej: "correcto-caballo-batería")
 
Esto responde a un debate real en seguridad informática: hay quienes
priorizan la entropía teórica máxima (contraseñas aleatorias con símbolos)
y quienes priorizan la memorabilidad real (passphrases largas), ya que
una contraseña muy compleja pero difícil de recordar termina anotada
en un papel o repetida en varios sitios, lo cual reduce la seguridad
real más de lo que la complejidad teórica la aumenta.
 
La fortaleza se calcula con un criterio cuantitativo (entropía en bits,
basada en el espacio de búsqueda), no solo con reglas simples como
"si tiene 3 tipos de caracteres es fuerte".
 
Materia: Lógica de Programación
"""
 
import random
import string
import math
 
 
# Lista corta de palabras para el modo passphrase
PALABRAS = [
    "casa", "rio", "sol", "luna", "tigre", "monte", "verde", "rapido",
    "fuego", "piedra", "nube", "viento", "lobo", "puente", "norte",
    "estrella", "camino", "fuerte", "azul", "rojo", "bosque", "isla",
    "trueno", "cristal", "sombra", "llama", "raiz", "torre", "espejo",
    "filo", "ancla", "brisa", "cumbre", "dragon", "valle", "marea"
]
 
 
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
    for _ in range(longitud):
        caracter = random.choice(caracteres_disponibles)
        contrasena += caracter
    return contrasena
 
 
def pedir_cantidad_palabras():
    """Pide cuántas palabras tendrá la passphrase, con validación."""
    while True:
        entrada = input("¿Cuántas palabras tendrá la passphrase? (mínimo 3, máximo 8): ")
        if entrada.isdigit():
            cantidad = int(entrada)
            if 3 <= cantidad <= 8:
                return cantidad
            else:
                print("Error: la cantidad debe estar entre 3 y 8. Intenta de nuevo.\n")
        else:
            print("Error: debes ingresar un número entero. Intenta de nuevo.\n")
 
 
def generar_passphrase(cantidad_palabras):
    """
    Genera una passphrase eligiendo palabras aleatorias de la lista
    y uniéndolas con guiones. Cada palabra se elige con un bucle.
    Se agrega un número al final para aumentar un poco la entropía.
    """
    palabras_elegidas = []
    for _ in range(cantidad_palabras):
        palabra = random.choice(PALABRAS)
        palabras_elegidas.append(palabra)
 
    numero_extra = random.randint(10, 99)
    passphrase = "-".join(palabras_elegidas) + "-" + str(numero_extra)
    return passphrase, cantidad_palabras
 
 
def calcular_entropia_caracteres(longitud, tamano_set):
    """
    Calcula la entropía en bits de una contraseña de caracteres aleatorios.
    Fórmula: entropía = longitud * log2(tamaño del set de caracteres)
    A mayor entropía, más intentos necesitaría un atacante por fuerza bruta.
    """
    if tamano_set <= 1:
        return 0
    return longitud * math.log2(tamano_set)
 
 
def calcular_entropia_passphrase(cantidad_palabras):
    """
    Calcula la entropía en bits de una passphrase.
    Fórmula: entropía = cantidad_palabras * log2(tamaño del diccionario de palabras)
    """
    return cantidad_palabras * math.log2(len(PALABRAS))
 
 
def clasificar_fortaleza(entropia_bits):
    """
    Clasifica la fortaleza según la entropía calculada, usando
    referencias generales de seguridad informática:
    - Menos de 40 bits: Débil (vulnerable a fuerza bruta en poco tiempo)
    - Entre 40 y 60 bits: Media
    - Más de 60 bits: Fuerte
    """
    if entropia_bits < 40:
        return "Débil"
    elif entropia_bits < 60:
        return "Media"
    else:
        return "Fuerte"
 
 
def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("\n========== GENERADOR DE CONTRASEÑAS ==========")
    print("1. Generar contraseña aleatoria (caracteres)")
    print("2. Generar passphrase (frase de palabras)")
    print("3. Salir")
    return input("Elige una opción (1/2/3): ").strip()
 
 
def main():
    """Función principal: controla el flujo del programa."""
    print("Bienvenido al Generador de Contraseñas")
    print("Puedes elegir entre una contraseña de caracteres aleatorios")
    print("o una passphrase (más fácil de recordar, igual de segura si es lo bastante larga).")
 
    while True:
        opcion = mostrar_menu()
 
        if opcion == "1":
            longitud = pedir_longitud()
            tipos = pedir_tipos()
            caracteres_disponibles = construir_set_caracteres(tipos)
 
            contrasena = generar_contrasena(longitud, caracteres_disponibles)
            entropia = calcular_entropia_caracteres(longitud, len(caracteres_disponibles))
            fortaleza = clasificar_fortaleza(entropia)
 
            print("\n--- Resultado ---")
            print(f"Contraseña generada: {contrasena}")
            print(f"Entropía estimada: {entropia:.1f} bits")
            print(f"Fortaleza: {fortaleza}")
 
        elif opcion == "2":
            cantidad_palabras = pedir_cantidad_palabras()
            passphrase, cantidad = generar_passphrase(cantidad_palabras)
            entropia = calcular_entropia_passphrase(cantidad)
            fortaleza = clasificar_fortaleza(entropia)
 
            print("\n--- Resultado ---")
            print(f"Passphrase generada: {passphrase}")
            print(f"Entropía estimada: {entropia:.1f} bits")
            print(f"Fortaleza: {fortaleza}")
 
        elif opcion == "3":
            print("\nGracias por usar el Generador de Contraseñas. ¡Hasta luego!")
            break
 
        else:
            print("\nOpción no válida. Por favor elige 1, 2 o 3.")
 
 
if __name__ == "__main__":
    main()
