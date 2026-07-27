def show_menu():
    print("\n----- Student Management System -----")
    print("1. Add student")
    print("2. Show all students")
    print("3. Show top 3 students")
    print("4. Show general average")
    print("5. Export data to CSV")
    print("6. Import data from CSV")
    print("0. Exit")

def get_option():
    option = -1
    try: 
        option = int(input("Select and option: "))
        if option not in [0, 1, 2, 3, 4, 5, 6]:
            raise ValueError()
    except Exception:
        print("Invalid option")
    return option