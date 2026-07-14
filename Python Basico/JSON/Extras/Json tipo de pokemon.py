import json

def read_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def filter_by_type(pokemon_list, pokemon_type):
    print(f"\nThe Pokemon of that type are:")
    found = False
    for pokemon in pokemon_list:
        if pokemon['type'].lower() == pokemon_type.lower():
            print(pokemon['name'])
            found = True
    if not found:
        print("No Pokemon found of that type.")

def main():
    file_path = input("Enter the JSON file path: ")
    pokemon_type = input("Enter the Pokemon type (Water, Fire, Electric, etc): ")
    pokemon_list = read_pokemon(file_path)
    filter_by_type(pokemon_list, pokemon_type)

main()