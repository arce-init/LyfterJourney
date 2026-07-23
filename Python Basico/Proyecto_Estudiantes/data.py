import csv
import os

def export_data(students, file_path):
    if not students:
        print("No students to export.")
        return
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = students[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students)
    print(f"Data exported to {file_path}")

def import_data(file_path):
    if not os.path.exists(file_path):
        print("No exported file found")
        return[]
    students = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name": row["name"],
                "section": row["section"],
                "spanish": float(row["spanish"]),
                "english": float(row["english"]),
                "social": float(row["social"]),
                "science": float(row["science"])
            })
    print(f"Data imported from {file_path}")
    return students