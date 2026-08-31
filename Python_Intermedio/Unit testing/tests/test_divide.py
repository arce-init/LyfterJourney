import pytest
from my_module.divide import divide


def test_divide_returns_correct_result():
    # Arrange
    number1 = 10
    number2 = 2

    # Act
    result = divide(number1, number2)

    # Assert
    assert result == 5.0


def test_divide_by_zero_raises_value_error():
    # Arrange
    number1 = 10
    number2 = 0

    # Act & Assert
    with pytest.raises(ValueError):
        divide(number1, number2)


def test_divide_with_string_raises_type_error():
    # Arrange
    number1 = 10
    number2 = "hola"

    # Act & Assert
    with pytest.raises(TypeError):
        divide(number1, number2)