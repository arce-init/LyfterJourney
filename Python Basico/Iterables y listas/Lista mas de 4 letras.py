my_list = []
for i in range(5):
    word = input("Enter 5 words: ")
    my_list.append(word)


new_list = []
for word in my_list:
    if len(word) > 4:
        new_list.append(word)

print(new_list)

