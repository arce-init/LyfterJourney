def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def count_upper_and_lower(text):
    upper_count = 0
    lower_count = 0

    for character in text:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1

    return f"There's {upper_count} upper cases and {lower_count} lower cases"


def sort_hyphenated_words(text):
    words_list = text.split("-")
    words_list.sort()
    return "-".join(words_list)


def get_prime_numbers(numbers_list):
    result_list = []

    for number in numbers_list:
        if is_prime(number):
            result_list.append(number)

    return result_list