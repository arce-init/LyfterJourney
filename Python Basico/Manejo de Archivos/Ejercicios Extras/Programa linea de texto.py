def append_to_file(file_path, text):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text + "\n")

def main():
    file_path = input("Enter the file path: ")
    text = input("Enter a line of text: ")
    append_to_file(file_path, text)
    print("Text added successfully!")

main()