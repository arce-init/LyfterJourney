import csv
from datetime import datetime, date


class Category:

    def __init__(self, name, color="#FFFFFF"):
        self.name = name
        self.color = color

    def to_dict(self):
        return {"name": self.name, "color": self.color}


class Transaction:

    def __init__(self, title, amount, category, transaction_type, transaction_date):
        self.title = title
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.transaction_date = transaction_date

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type,
            "transaction_date": self.transaction_date
        }


def is_valid_date_format(date_string):
    try:
        datetime.strptime(date_string, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def is_future_date(date_string):
    parsed_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    return parsed_date > date.today()


class FinanceManager:

    def __init__(self):
        self.categories = []
        self.transactions = []

    def add_category(self, name, color="#FFFFFF"):
        if not name or name.strip() == "":
            raise ValueError("Category name cannot be empty")

        new_category = Category(name, color)
        self.categories.append(new_category)
        return new_category

    def get_category_names(self):
        return [category.name for category in self.categories]

    def get_category_color(self, name):
        for category in self.categories:
            if category.name == name:
                return category.color
        return "#FFFFFF"

    def add_transaction(self, title, amount, category, transaction_type, transaction_date=None):
        if len(self.categories) == 0:
            raise ValueError("No categories available. You must create one first.")

        if not title or title.strip() == "":
            raise ValueError("Title cannot be empty")

        if category not in self.get_category_names():
            raise ValueError(f"Category '{category}' does not exist")

        if transaction_date is None:
            transaction_date = date.today().strftime("%d/%m/%Y")

        if not is_valid_date_format(transaction_date):
            raise ValueError("Invalid date format (use dd/mm/yyyy)")

        if is_future_date(transaction_date):
            raise ValueError("Date cannot be in the future")

        new_transaction = Transaction(title, amount, category, transaction_type, transaction_date)
        self.transactions.append(new_transaction)
        return new_transaction

    def calculate_balance(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.amount
        return total

    def filter_transactions_by_date(self, start_date_str, end_date_str):
        if not is_valid_date_format(start_date_str) or not is_valid_date_format(end_date_str):
            raise ValueError("Invalid date format (use dd/mm/yyyy)")

        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

        filtered = []
        for transaction in self.transactions:
            transaction_date = datetime.strptime(transaction.transaction_date, "%d/%m/%Y").date()
            if start_date <= transaction_date <= end_date:
                filtered.append(transaction)

        return filtered

    def export_to_csv(self, file_path):
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])

            total_income = 0
            total_expense = 0

            for transaction in self.transactions:
                writer.writerow([
                    transaction.transaction_date,
                    transaction.title,
                    transaction.amount,
                    transaction.category,
                    transaction.transaction_type
                ])
                if transaction.transaction_type == "Income":
                    total_income += transaction.amount
                else:
                    total_expense += abs(transaction.amount)

            writer.writerow([])
            writer.writerow(["Totales:"])
            writer.writerow([f"Ingresos: {total_income}"])
            writer.writerow([f"Gastos: {total_expense}"])
            writer.writerow([f"Balance Neto: {total_income - total_expense}"])