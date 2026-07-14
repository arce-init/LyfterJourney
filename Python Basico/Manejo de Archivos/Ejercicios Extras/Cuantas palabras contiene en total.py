def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return len(content.split())

def main():
    file_path = input("Enter the file path: ")
    total = count_words(file_path)
    print(f"This file contains {total} words")

main()