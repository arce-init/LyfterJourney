import csv

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['Name']}")
            print(f"Genre: {row['Genre']}")
            print(f"Developer: {row['Developer']}")
            print(f"ESRB Rating: {row['ESRB Rating']}")
            print()

def main():
    file_path = input("Enter the CSV file path: ")
    read_games(file_path)

main()