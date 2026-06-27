# Gener@Pass — Generador de Contraseñas Seguras

> Proyecto Integrador — Lógica de Programación  
> Universidad Internacional del Ecuador (UIDE)

---

## Nombre del proyecto

**Gener@Pass: Sistema Generador de Contraseñas Seguras**

Desarrollado como proyecto integrador de la asignatura Lógica de Programación, en el marco del tema:  
*"El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas"*

---

## Estudiante

**Leandro Jharley Alcívar Sornoza**  
Docente: Paulina Vizcaíno  
Fecha de entrega: 28 de junio de 2026

---

## Objetivo del sistema

Desarrollar un sistema funcional en Python que permita generar contraseñas y passphrases seguras de forma personalizada, calculando su fortaleza mediante un criterio científico basado en entropía real (bits), con el fin de responder a la necesidad de seguridad digital en un entorno donde la mayoría de brechas de seguridad se originan en contraseñas débiles o reutilizadas.

---

## Descripción de funcionalidades

### Modo 1 — Contraseña aleatoria
- El usuario elige la **longitud** (entre 4 y 64 caracteres)
- El usuario elige qué **tipos de caracteres** incluir: mayúsculas, minúsculas, números y/o símbolos
- El sistema genera la contraseña **carácter por carácter** mediante un bucle `for`
- Valida que al menos un tipo de carácter esté seleccionado

### Modo 2 — Passphrase
- El usuario elige la **cantidad de palabras** (entre 3 y 8)
- El sistema selecciona palabras al azar de un diccionario interno
- Las une con guiones y agrega un número aleatorio al final
- Ejemplo: `correcto-caballo-batería-42`

### Evaluación de fortaleza (entropía real)
- Calcula la entropía en bits usando la fórmula: **H = L × log₂(N)**
  - L = longitud de la contraseña
  - N = tamaño del conjunto de símbolos disponibles
- Clasifica el resultado como:
  - 🔴 **Débil** — menos de 40 bits
  - 🟡 **Media** — entre 40 y 60 bits
  - 🟢 **Fuerte** — más de 60 bits

### Validación de entradas
- Bucles `while` y condicionales validan todos los datos ingresados por el usuario
- Evita errores de ejecución por entradas incorrectas

### Menú repetitivo
- Permite generar múltiples contraseñas en una sola sesión sin reiniciar el programa

---

## Integración de las 4 unidades del curso

| Unidad | Contenido aplicado | Dónde se evidencia |
|--------|-------------------|-------------------|
| **U1 — Estructuras lógicas** | `if / elif / else`, operadores lógicos | Validaciones y clasificación de fortaleza |
| **U2 — Programación estructurada** | `while`, `for`, funciones | Menú, generación de caracteres y palabras |
| **U3 — Fundamentos de POO** | Separación de responsabilidades | 10 funciones con responsabilidad única |
| **U4 — Herramientas de desarrollo** | GitHub, README, librerías estándar | Repositorio con historial de commits |

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Librerías:** `random`, `string`, `math` (estándar, sin instalación adicional)
- **Control de versiones:** Git y GitHub
- **Entorno:** Visual Studio Code

---

## Cómo ejecutarlo

1. Verifica que tienes Python 3 instalado:
   ```
   python3 --version
   ```
2. Clona el repositorio:
   ```
   git clone https://github.com/tu-usuario/generador-contrasenas.git
   ```
3. Ejecuta el programa:
   ```
   python3 generador_contrasenas.py
   ```
4. Sigue las instrucciones en pantalla

---

## Estructura del proyecto

```
├── generador_contrasenas.py   # Código principal del programa
├── diagrama_flujo.svg         # Diagrama de flujo (vectorial)
├── diagrama_flujo.jpg         # Diagrama de flujo (imagen)
└── README.md                  # Este archivo
```

---

## Estado del proyecto

✅ **Completado** — Proyecto integrador Semana 8, Lógica de Programación, UIDE 2026
