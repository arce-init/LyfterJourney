from my_module.string_functions import count_upper_and_lower, sort_hyphenated_words, get_prime_numbers


# --- Ejercicio 3: count_upper_and_lower ---

def test_count_upper_and_lower_with_mixed_text():
    # Arrange
    input_text = "I love Nación Sushi"

    # Act
    result = count_upper_and_lower(input_text)

    # Assert
    assert result == "There's 3 upper cases and 13 lower cases"


def test_count_upper_and_lower_with_all_lowercase():
    # Arrange
    input_text = "hello world"

    # Act
    result = count_upper_and_lower(input_text)

    # Assert
    assert result == "There's 0 upper cases and 10 lower cases"


def test_count_upper_and_lower_with_all_uppercase():
    # Arrange
    input_text = "HELLO"

    # Act
    result = count_upper_and_lower(input_text)

    # Assert
    assert result == "There's 5 upper cases and 0 lower cases"


# --- Ejercicio 4: sort_hyphenated_words ---

def test_sort_hyphenated_words_with_example_from_exercise():
    # Arrange
    input_text = "python-variable-funcion-computadora-monitor"

    # Act
    result = sort_hyphenated_words(input_text)

    # Assert
    assert result == "computadora-funcion-monitor-python-variable"


def test_sort_hyphenated_words_with_two_words():
    # Arrange
    input_text = "banana-apple"

    # Act
    result = sort_hyphenated_words(input_text)

    # Assert
    assert result == "apple-banana"


def test_sort_hyphenated_words_with_already_sorted_words():
    # Arrange
    input_text = "apple-banana-cherry"

    # Act
    result = sort_hyphenated_words(input_text)

    # Assert
    assert result == "apple-banana-cherry"


# --- Ejercicio 5: get_prime_numbers ---

def test_get_prime_numbers_with_example_from_exercise():
    # Arrange
    input_list = [1, 4, 6, 7, 13, 9, 67]

    # Act
    result = get_prime_numbers(input_list)

    # Assert
    assert result == [7, 13, 67]


def test_get_prime_numbers_with_no_primes():
    # Arrange
    input_list = [1, 4, 6, 8, 9, 10]

    # Act
    result = get_prime_numbers(input_list)

    # Assert
    assert result == []


def test_get_prime_numbers_with_all_primes():
    # Arrange
    input_list = [2, 3, 5, 11]

    # Act
    result = get_prime_numbers(input_list)

    # Assert
    assert result == [2, 3, 5, 11]