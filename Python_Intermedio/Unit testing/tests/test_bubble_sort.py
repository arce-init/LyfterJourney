import pytest
from my_module.bubble_sort import bubble_sort


def test_bubble_sort_with_small_list():
    # Arrange
    input_list = [5, 3, 4, 1, 2]

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == [1, 2, 3, 4, 5]


def test_bubble_sort_with_large_list():
    # Arrange
    input_list = list(range(150, 0, -1))

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == list(range(1, 151))


def test_bubble_sort_with_empty_list():
    # Arrange
    input_list = []

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == []


def test_bubble_sort_throws_exception_with_non_list_parameter():
    # Arrange
    input_value = "not a list"

    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(input_value)