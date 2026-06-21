Programa desarrollado en Python para la materia **Lógica de Programación**, que permite generar contraseñas seguras de forma personalizada.

## Descripción

El usuario puede elegir la longitud de la contraseña y qué tipos de caracteres incluir (mayúsculas, minúsculas, números y símbolos). El programa valida las entradas, genera la contraseña carácter por carácter y evalúa su nivel de fortaleza (Débil, Media, Fuerte). Además, permite generar varias contraseñas seguidas sin tener que reiniciar el programa.

## Funcionalidades

- Menú interactivo (generar contraseña / salir)
- Validación de longitud (entre 4 y 64 caracteres)
- Selección de tipos de caracteres a incluir
- Validación para evitar generar una contraseña vacía (sin tipos seleccionados)
- Generación aleatoria de la contraseña
- Medidor de fortaleza según longitud y variedad de caracteres
- Opción de generar múltiples contraseñas en una misma ejecución

## Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Librerías:** `random`, `string` (incluidas en la librería estándar de Python, no requieren instalación)

## Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado. Puedes verificarlo con:
   ```
   python3 --version
   ```
2. Clona o descarga este repositorio.
3. Desde la terminal, ubícate en la carpeta del proyecto y ejecuta:
   ```
   python3 generador_contrasenas.py
   ```
4. Sigue las instrucciones que aparecen en pantalla.

## Estructura del proyecto

```
├── generador_contrasenas.py   # Código principal del programa
├── diagrama_flujo.svg         # Diagrama de flujo de la lógica del programa
├── diagrama_flujo.jpg         # Diagrama de flujo en formato imagen
└── README.md                  # Este archivo
```

## Diagrama de flujo

El diagrama de flujo (`diagrama_flujo.jpg` / `diagrama_flujo.svg`) muestra el recorrido lógico del programa: desde el menú principal, pasando por la validación de datos, el ciclo de generación de caracteres, hasta el cálculo de la fortaleza y la opción de repetir el proceso.

## Estado del proyecto

🔧 En desarrollo — proyecto académico para la materia Lógica de Programación.

## Autor

Proyecto desarrollado como entrega para la materia Lógica de Programación.
md…]()
