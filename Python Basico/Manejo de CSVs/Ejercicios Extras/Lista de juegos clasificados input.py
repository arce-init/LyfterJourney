import csv

def read_games(file_path):
    games = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            games.append(row)
    return games

def filter_by_rating(games, rating):
    for game in games:
        if game['ESRB Rating'] == rating:
            print(f"Name: {game['Name']}")
            print(f"Genre: {game['Genre']}")
            print(f"Developer: {game['Developer']}")
            print(f"ESRB Rating: {game['ESRB Rating']}")
            print()

def main():
    file_path = input("Enter the CSV file path: ")
    rating = input("Enter ESRB rating to filter (E, T, M...): ")
    games = read_games(file_path)
    filter_by_rating(games, rating)

main()