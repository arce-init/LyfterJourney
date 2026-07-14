import json

def read_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_new_pokemon():
    name = input("Name: ")
    type_ = input("Type: ")
    level = int(input("Level: "))
    weight = float(input("Weight (kg): "))
    is_shiny = input("Is Shiny? (yes/no): ").lower() == "yes"

    skills = []
    n = int(input("How many skills? "))
    for i in range(n):
        skills.append(input(f"Skill {i+1}: "))

    return {
        "name": name,
        "type": type_,
        "level": level,
        "weight_kg": weight,
        "is_shiny": is_shiny,
        "held_item": None,
        "skills": skills,
        "stats": {
            "hp": int(input("HP: ")),
            "attack": int(input("Attack: ")),
            "defense": int(input("Defense: ")),
            "sp_attack": int(input("Sp. Attack: ")),
            "sp_defense": int(input("Sp. Defense: ")),
            "speed": int(input("Speed: "))
            }
        }

def save_pokemon(file_path, pokemon_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(pokemon_list, file, indent=4)

def main():
    file_path = input("Enter the JSON file path: ")
    pokemon_list = read_pokemon(file_path)
    new_pokemon = get_new_pokemon()
    pokemon_list.append(new_pokemon)
    save_pokemon(file_path, pokemon_list)
    print(f"{new_pokemon['name']} added successfully!")

main()