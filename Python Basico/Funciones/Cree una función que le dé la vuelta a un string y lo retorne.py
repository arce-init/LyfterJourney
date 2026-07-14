def reverse_string(my_string):
    result = ""
    for i in range(len(my_string) - 1, -1, -1):
        result = result + my_string[i]
    return result

print(reverse_string("Hello World"))