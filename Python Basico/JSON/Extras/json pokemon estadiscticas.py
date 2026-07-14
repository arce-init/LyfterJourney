import json

def read_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def show_stats(pokemon_list):
    for pokemon in pokemon_list:
        print(f"Name: {pokemon['name']}")
        print(f"Attack: {pokemon['stats']['attack']}")
        print(f"Defense: {pokemon['stats']['defense']}")
        print(f"Speed: {pokemon['stats']['speed']}")
        print()

def main():
    file_path = input("Enter the JSON file path: ")
    pokemon_list = read_pokemon(file_path)
    show_stats(pokemon_list)

main()