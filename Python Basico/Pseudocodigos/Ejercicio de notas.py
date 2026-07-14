total_grades = 0
grade_counter = 1
current_grade = 0
approved_count = 0
failed_count = 0
approved_average = 0
failed_average = 0
total_average = 0

total_grades = int(input("Enter the number of grades: "))

while grade_counter <= total_grades:
    print("Enter grade number")
    print(grade_counter)
    current_grade = int(input("Current grade: "))
    if current_grade < 70:
        failed_count = failed_count + 1
        failed_average = failed_average + current_grade
    else:
        approved_count = approved_count + 1
        approved_average = approved_average + current_grade
    total_average = total_average + current_grade
    grade_counter = grade_counter + 1

if failed_count > 0:
    failed_average = failed_average / failed_count
else:
    failed_average = 0
    print("No failed grades")

if approved_count > 0:
    approved_average = approved_average / approved_count
else:
    approved_average = 0
    print("No approved grades")

total_average = total_average / total_grades


print("The student has this many approved grades:")
print(approved_count)
print("This is the average of approved grades:")
print(approved_average)
print("The student has this many failed grades:")
print(failed_count)
print("This is the average of failed grades:")
print(failed_average)
print("This is the overall grade average:")
print(total_average)