import json
import os


def save_data(finance_manager, file_path="finance_data.json"):
    data = {
        "categories": [category.to_dict() for category in finance_manager.categories],
        "transactions": [transaction.to_dict() for transaction in finance_manager.transactions]
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data(finance_manager, file_path="finance_data.json"):
    if not os.path.exists(file_path):
        return finance_manager

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for category_dict in data.get("categories", []):
        finance_manager.add_category(
            category_dict["name"],
            category_dict.get("color", "#FFFFFF")
        )

    for transaction_dict in data.get("transactions", []):
        finance_manager.add_transaction(
            transaction_dict["title"],
            transaction_dict["amount"],
            transaction_dict["category"],
            transaction_dict["transaction_type"],
            transaction_dict.get("transaction_date")
        )

    return finance_manager