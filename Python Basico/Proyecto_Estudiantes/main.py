from menu import show_menu, get_option
from actions import add_students, show_students, show_top_3, show_general_average
from data import export_data, import_data

def main():
    students = []
    file_path = "students.csv"

    while True:
        show_menu()
        option = get_option()

        if option == -1:
            continue
        elif option == 1:
            add_students(students)
        elif option == 2:
            show_students(students)
        elif option == 3:
            show_top_3(students)
        elif option == 4:
            show_general_average(students)
        elif option == 5:
            export_data(students, file_path)
        elif option == 6:
            students = import_data(file_path)
        elif option == 0:
            print("Goodbye!")
            break


main()