import csv

def get_games(n):
    games = []
    for i in range(n):
        print(f"\nGame {i + 1}:")
        game = {
            "Name": input("Name: "),
            "Genre": input("Genre: "),
            "Developer": input("Developer: "),
            "ESRB Rating": input("ESRB Rating: ")
        }
        games.append(game)
    return games

def save_games_info(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

def main():
    n = int(input("How many games do you want to add? "))
    game_list = get_games(n)
    save_games_info('game_ranking.tsv', game_list)
    print("Done! Check game_ranking.tsv")

main()