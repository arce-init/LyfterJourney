def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def to_uppercase(lines):
    return [line.strip().upper() for line in lines]

def write_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + "\n")

def main():
    input_path = input("Enter the input file path: ")
    output_path = input("Enter the output file path: ")
    lines = read_file(input_path)
    upper_lines = to_uppercase(lines)
    write_file(output_path, upper_lines)
    print("Done!")

main()