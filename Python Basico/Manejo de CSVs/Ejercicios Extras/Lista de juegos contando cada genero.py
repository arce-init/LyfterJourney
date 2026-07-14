import csv

def read_games(file_path):
    games = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            games.append(row)
    return games

def count_by_genre(games):
    genres = {}
    for game in games:
        genre = game['Genre']
        if genre in genres:
            genres[genre] = genres[genre] + 1
        else:
            genres[genre] = 1
    return genres

def show_results(genres):
    print("Genres found:")
    for genre, count in sorted(genres.items()):
        print(f"{genre}: {count}")

def main():
    file_path = input("Enter the CSV file path: ")
    games = read_games(file_path)
    genres = count_by_genre(games)
    show_results(genres)

main()