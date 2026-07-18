def get_average(student):
    return (student["spanish"] + student["english"] + student["social"] + student["science"])/4

def add_students(students):
    name = input("Full name: ").strip()
    section = input("Section (ex: 11B): ").strip()

    spanish = get_valid_grade("Spanish grade: ")
    english = get_valid_grade("English grade: ")
    social = get_valid_grade("Social studies grade: ")
    science = get_valid_grade("Science grade: ")

    students.append({
        "name": name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "social": social,
        "science": science
    })
    print(f"Student {name} added successfully!")

def get_valid_grade(prompt):
    grade = -1
    while grade < 0 or grade > 100:
        try:
            grade = float(input(prompt))
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100")
        except ValueError:
            print("Invalid grade, enter a number")
            grade = -1
    return grade

def show_students(students):
    if not students:
        print("No students registered")
        return
    for student in students:
        avg = get_average(student)
        print(f"\nName: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish']}")
        print(f"English: {student['english']}")
        print(f"Social: {student['social']}")
        print(f"Science: {student['science']}")
        print(f"Average: {avg:2f}")

def show_top_3(students):
    if not students:
        print("No students registered")
        return
    sorted_students = sorted(students, key=get_average, reverse=True)
    print("\nTop 3 students:")
    for i, student in enumerate(sorted_students[:3]):
        print(f"{i+1}. {student['name']} - Average: {get_average(student):.2f}")

def show_general_average(students):
    if not students:
        print("No students registered")
        return
    total = sum(get_average(s) for s in students)
    general_avg = total / len(students)
    print(f"\nGeneral average of all students: {general_avg:.2f}")