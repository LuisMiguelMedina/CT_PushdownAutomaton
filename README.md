# Pushdown Automaton Documentation [ES]

## Clase `stack`

La clase `Stack` representa una pila, una estructura de datos que sigue el principio de último en entrar, primero en salir (LIFO).

### Métodos

- `__init__(self)`
  - Descripción: Inicializa una nueva instancia de Stack con una lista vacía.
  - Parámetros: Ninguno.

- `push(self, item)`
  - Descripción: Añade un elemento al final de la pila.
  - Parámetros:
    - `item`: El elemento a añadir.

- `pop(self)`
  - Descripción: Elimina y devuelve el último elemento de la pila.
  - Parámetros: Ninguno.
  - Retorna: El último elemento de la pila, o `None` si la pila está vacía.

- `peek(self)`
  - Descripción: Devuelve el último elemento de la pila sin eliminarlo.
  - Parámetros: Ninguno.
  - Retorna: El último elemento de la pila, o `None` si la pila está vacía.

- `is_empty(self)`
  - Descripción: Comprueba si la pila está vacía.
  - Parámetros: Ninguno.
  - Retorna: `True` si la pila está vacía, de lo contrario `False`.

## Clase `palidrome`

La clase `PalindromePDA` representa un autómata de pila que verifica si una secuencia de tokens forma un palíndromo de longitud par.

### Atributos

- `stack`: Una instancia de la clase `Stack` utilizada para almacenar tokens durante el proceso de verificación.

### Métodos

- `__init__(self)`
  - Descripción: Inicializa el autómata con una pila.
  - Parámetros: Ninguno.

- `process_tokens(self, tokens)`
  - Descripción: Procesa una secuencia de tokens para determinar si forman un palíndromo de longitud par.
  - Parámetros:
    - `tokens`: Una lista de tokens para verificar.
  - Retorna: `True` si los tokens forman un palíndromo de longitud par, de lo contrario `False`.

## Clase `Simulator`

### -> Función `input_string`

Esta función recoge la entrada del usuario y la convierte en tokens utilizando un lexer.

### Parámetros

- `lexer`: Una instancia de lexer para procesar la entrada del usuario.

### Retorno

- Retorna una tupla que contiene la lista de tokens y un booleano que indica si se encontró algún carácter ilegal.

### -> Función `simulate_pda`

Esta función simula el autómata de pila, interactuando con el usuario y procesando las cadenas ingresadas.

### Parámetros

- `lexer`: Una instancia del lexer para tokenizar la entrada del usuario.

### Funcionalidad

- Solicita al usuario que ingrese una cadena.
- Usa el lexer para convertir la entrada en tokens.
- Verifica si la cadena es un palíndromo de longitud par utilizando `PalindromePDA`.
- Imprime el resultado de la verificación.

## Lexer y Tokens

La configuración del lexer y los tokens que define qué caracteres son válidos para el autómata (en este caso 'A' y 'B' y sus equivalentes en minúsculas).

### Tokens

- `"A"` y `"B"`: Representan los caracteres válidos.

### Reglas del Lexer

- `t_A`: Define el token para el carácter 'a'.
- `t_B`: Define el token para el carácter 'b'.
- `t_ignore`: Caracteres a ignorar (espacios y tabulaciones).
- `t_error`: Función para manejar caracteres no válidos.

---

