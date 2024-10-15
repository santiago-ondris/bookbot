# Analizador de Texto Simple en Python

Este script analiza un archivo de texto para contar las palabras y los caracteres que contiene.  Es un proyecto sencillo, ideal para principiantes en Python.

## Funcionalidad

El script lee un archivo de texto especificado, cuenta las palabras y realiza un recuento de los caracteres alfabéticos, mostrando luego un reporte con la cantidad de palabras y la frecuencia de cada caracter alfabético.

## Uso

1. **Requisitos:** Python 3.x.
2. **Ejecución:** Ejecuta el script desde la línea de comandos: `python main.py`.
3. **Archivo de entrada:** El script busca un archivo llamado `books/frankenstein.txt` en la misma carpeta. Este archivo existe en la ruta especificada.

## Estructura del código

El código está organizado en las siguientes funciones:

* `read_file(path)`: Lee el contenido del archivo especificado.
* `count_words(text)`: Cuenta las palabras en el texto.
* `count_characters(text)`: Cuenta la frecuencia de cada carácter alfabético en el texto (en minúsculas).
* `generate_report(path, word_count, char_counts)`: Genera y muestra un informe con los resultados.
* `main()`: Función principal que orquesta las otras funciones.

