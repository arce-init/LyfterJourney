def read_songs(file_path):
    songs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        songs = file.readlines()
    return [song.strip() for song in songs]

def sort_songs(songs):
    songs.sort()
    return songs

def write_songs(file_path, songs):
    with open(file_path, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + "\n")

def main():
    input_path = input("Enter the input file path: ")
    output_path = input("Enter the output file path: ")
    
    songs = read_songs(input_path)
    songs = sort_songs(songs)
    write_songs(output_path, songs)
    
    print("Done! Check the output file")

main()