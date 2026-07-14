def count_character(text, character):
    count = 0
    for letter in text:
        if letter == character:
            count = count + 1
    return count

result = count_character("programacion", "o")
print(f"Se ha encontrado {result} veces el carácter")