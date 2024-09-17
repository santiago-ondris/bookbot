def main():
    path = "books/frankenstein.txt"
    file_contents = read_file(path)
    word_count = count_words(file_contents)
    char_counts = count_characters(file_contents)
    generate_report(path, word_count, char_counts)

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split() # Se convierte el texto a una lista de palabras
    return len(words) # Se cuentan las palabras

def count_characters(text):
    char_counts = {} # Creo un diccionario
    for char in text.lower(): # Itero por cada caracter del texto
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def generate_report(path, word_count, char_counts):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")


    """Creo una lista vacía llamada char_list.
    Se itera sobre cada par clave-valor en char_counts usando el método .items().
    Para cada par, se crea un nuevo diccionario char_dict con dos claves: "char" y "count".
    Se añade este nuevo diccionario a nuestra lista char_list."""

    char_list = []
    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)

    # Se imprimen los caracteres contados
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()


