import pytest
from unittest.mock import patch, mock_open
from my_module.read_lines import read_lines


def test_read_lines_returns_expected_lines():
    # Arrange
    fake_file_content = "line 1\nline 2\nline 3\n"

    # Act
    with patch("builtins.open", mock_open(read_data=fake_file_content)):
        result = read_lines("fake_path.txt")

    # Assert
    assert result == ["line 1\n", "line 2\n", "line 3\n"]


def test_read_lines_raises_file_not_found_error():
    # Arrange
    non_existent_path = "this_file_does_not_exist.txt"

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        read_lines(non_existent_path)