import pytest
from logic import FinanceManager


def test_add_category_success():
    # Arrange
    manager = FinanceManager()

    # Act
    manager.add_category("Food")

    # Assert
    assert manager.get_category_names() == ["Food"]


def test_add_category_with_empty_name_raises_error():
    # Arrange
    manager = FinanceManager()

    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_category("")


def test_get_category_names_returns_multiple_categories():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Food")
    manager.add_category("Transport")

    # Act
    result = manager.get_category_names()

    # Assert
    assert result == ["Food", "Transport"]


def test_add_transaction_success():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Food")

    # Act
    manager.add_transaction("Pizza", -20, "Food", "Expense")

    # Assert
    assert len(manager.transactions) == 1
    assert manager.transactions[0].title == "Pizza"


def test_add_transaction_without_categories_raises_error():
    # Arrange
    manager = FinanceManager()

    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_transaction("Pizza", -20, "Food", "Expense")


def test_add_transaction_with_nonexistent_category_raises_error():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Food")

    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_transaction("Bus ticket", -5, "Transport", "Expense")


def test_add_transaction_with_empty_title_raises_error():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Food")

    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_transaction("", -20, "Food", "Expense")


def test_calculate_balance_with_income_and_expenses():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Food")
    manager.add_category("Work")
    manager.add_transaction("Salary", 1000, "Work", "Income")
    manager.add_transaction("Pizza", -20, "Food", "Expense")

    # Act
    result = manager.calculate_balance()

    # Assert
    assert result == 980


def test_calculate_balance_with_no_transactions_is_zero():
    # Arrange
    manager = FinanceManager()

    # Act
    result = manager.calculate_balance()

    # Assert
    assert result == 0