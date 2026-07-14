import csv

def read_games(file_path):
    games = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            games.append(row)
    return games

def filter_by_developer(games, developer):
    print(f"\nGames developed by {developer}:")
    found = False
    for game in games:
        if game['Developer'].lower() == developer.lower():
            print(f"- {game['Name']} (Rating: {game['ESRB Rating']}, Genre: {game['Genre']})")
            found = True
    if not found:
        print("No games found for this developer.")

def main():
    file_path = input("Enter the CSV file path: ")
    developer = input("Enter the developer name: ")
    games = read_games(file_path)
    filter_by_developer(games, developer)

main()