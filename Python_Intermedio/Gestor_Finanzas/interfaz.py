import FreeSimpleGUI as sg
from logic import FinanceManager
from datetime import date
from persistence import save_data, load_data


def build_table_data(finance_manager, transactions=None):
    if transactions is None:
        transactions = finance_manager.transactions

    table_data = []
    for transaction in transactions:
        table_data.append([
            transaction.transaction_date,
            transaction.title,
            transaction.amount,
            transaction.category,
            transaction.transaction_type
        ])
    return table_data


def build_row_colors(finance_manager, transactions=None):
    if transactions is None:
        transactions = finance_manager.transactions

    row_colors = []
    for index, transaction in enumerate(transactions):
        color = finance_manager.get_category_color(transaction.category)
        row_colors.append((index, color))
    return row_colors


def open_add_category_window(finance_manager):
    layout = [
        [sg.Text("Category name:"), sg.Input(key="-CATEGORY_NAME-")],
        [sg.Text("Color:"), sg.Input("#FFFFFF", key="-CATEGORY_COLOR-", size=(10, 1)),
        sg.ColorChooserButton("Choose", target="-CATEGORY_COLOR-")],
        [sg.Button("Save"), sg.Button("Cancel")],
    ]

    window = sg.Window("Add Category", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        elif event == "Save":
            try:
                finance_manager.add_category(values["-CATEGORY_NAME-"], values["-CATEGORY_COLOR-"])
                sg.popup("Category added successfully!")
                break
            except ValueError as error:
                sg.popup_error(str(error))

    window.close()


def open_add_transaction_window(finance_manager, transaction_type):
    if len(finance_manager.categories) == 0:
        sg.popup_error("No categories available. Please create one first.")
        return

    category_names = finance_manager.get_category_names()
    today_str = date.today().strftime("%d/%m/%Y")

    layout = [
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(category_names, key="-CATEGORY-")],
        [sg.Text("Date (dd/mm/yyyy):"), sg.Input(today_str, key="-DATE-")],
        [sg.Button("Save"), sg.Button("Cancel")],
    ]

    window = sg.Window(f"Add {transaction_type}", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        elif event == "Save":
            try:
                amount = float(values["-AMOUNT-"])
                if transaction_type == "Expense":
                    amount = -abs(amount)
                else:
                    amount = abs(amount)

                finance_manager.add_transaction(
                    values["-TITLE-"],
                    amount,
                    values["-CATEGORY-"],
                    transaction_type,
                    values["-DATE-"]
                )
                sg.popup(f"{transaction_type} added successfully!")
                break
            except ValueError as error:
                sg.popup_error(str(error))

    window.close()


def run_main_window():
    finance_manager = FinanceManager()
    finance_manager = load_data(finance_manager)

    headers = ["Date", "Title", "Amount", "Category", "Type"]

    layout = [
        [sg.Text("Personal Finance Manager", font=("Any", 16))],
        [sg.Table(
            values=build_table_data(finance_manager),
            headings=headers,
            key="-TABLE-",
            auto_size_columns=True,
            expand_x=True,
            num_rows=10,
            row_colors=build_row_colors(finance_manager)
        )],
        [sg.Text("Balance:"), sg.Text(finance_manager.calculate_balance(), key="-BALANCE-")],
        [sg.Button("Add Category"), sg.Button("Add Expense"), sg.Button("Add Income")],
        [sg.Text("From:"), sg.Input(key="-DATE_FROM-", size=(12, 1)),
        sg.Text("To:"), sg.Input(key="-DATE_TO-", size=(12, 1)),
        sg.Button("Filter"), sg.Button("Clear Filter")],
        [sg.Button("Export to CSV")],
    ]

    window = sg.Window("Personal Finance Manager", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "Add Category":
            open_add_category_window(finance_manager)
            window["-TABLE-"].update(build_table_data(finance_manager), row_colors=build_row_colors(finance_manager))
            window["-BALANCE-"].update(finance_manager.calculate_balance())

        elif event == "Add Expense":
            open_add_transaction_window(finance_manager, "Expense")
            window["-TABLE-"].update(build_table_data(finance_manager), row_colors=build_row_colors(finance_manager))
            window["-BALANCE-"].update(finance_manager.calculate_balance())

        elif event == "Add Income":
            open_add_transaction_window(finance_manager, "Income")
            window["-TABLE-"].update(build_table_data(finance_manager), row_colors=build_row_colors(finance_manager))
            window["-BALANCE-"].update(finance_manager.calculate_balance())

        elif event == "Filter":
            try:
                filtered = finance_manager.filter_transactions_by_date(values["-DATE_FROM-"], values["-DATE_TO-"])
                window["-TABLE-"].update(
                    build_table_data(finance_manager, filtered),
                    row_colors=build_row_colors(finance_manager, filtered)
                )
            except ValueError as error:
                sg.popup_error(str(error))

        elif event == "Clear Filter":
            window["-TABLE-"].update(build_table_data(finance_manager), row_colors=build_row_colors(finance_manager))

        elif event == "Export to CSV":
            finance_manager.export_to_csv("movements_export.csv")
            sg.popup("Data exported to movements_export.csv")

    save_data(finance_manager)
    window.close()