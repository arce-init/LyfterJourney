def filter_words(word_list, n):
    result = []
    for word in word_list:
        if len(word)> n:
            result.append(word)
    return result
my_list = ["sky", "sun", "wonderful", "day"]
n = int(input("Enter the minimum amount of letters in the word: "))
print(filter_words(my_list, n))
