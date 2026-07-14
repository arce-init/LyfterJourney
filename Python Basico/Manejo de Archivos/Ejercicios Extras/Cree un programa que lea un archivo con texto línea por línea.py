def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def join_lines(lines):
    return " ".join([line.strip() for line in lines])

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    input_path = input("Enter the input file path: ")
    output_path = input("Enter the output file path: ")
    lines = read_file(input_path)
    content = join_lines(lines)
    write_file(output_path, content)
    print("Done!")

main()