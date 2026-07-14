import json

def read_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def average_level_by_type(pokemon_list):
    types = {}
    for pokemon in pokemon_list:
        type_ = pokemon['type']
        level = pokemon['level']
        if type_ in types:
            types[type_].append(level)
        else:
            types[type_] = [level]

    for type_, levels in sorted(types.items()):
        average = sum(levels) / len(levels)
        print(f"Type: {type_} → Average level: {average:.1f}")

def main():
    file_path = input("Enter the JSON file path: ")
    pokemon_list = read_pokemon(file_path)
    average_level_by_type(pokemon_list)

main()