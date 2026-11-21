''' Activity 1, Task 2: CSV file operations (students.csv).'''
import csv

FILENAME = "students.csv"
FIELDS = ["id", "name", "course", "grade"]
STUDENTS = [
    {"id": "2021001", "name": "Juan Dela Cruz", "course": "BSCpE", "grade": 92.5},
    {"id": "2021002", "name": "Maria Santos",   "course": "BSCpE", "grade": 88.0},
    {"id": "2021003", "name": "Jose Reyes",     "course": "BSEE",  "grade": 79.5},
    {"id": "2021004", "name": "Ana Garcia",     "course": "BSCpE", "grade": 95.0},
    {"id": "2021005", "name": "Pedro Bautista", "course": "BSECE", "grade": 84.0},
]

def create_csv():
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(STUDENTS)
    print(f"[Created] {FILENAME} with {len(STUDENTS)} records.")

def display_csv():
    with open(FILENAME, newline="") as f:
        rows = list(csv.DictReader(f))
    print(f"{'ID':<10}{'Name':<20}{'Course':<10}{'Grade':>7}")
    print("-" * 47)
    for r in rows:
        print(f"{r['id']:<10}{r['name']:<20}{r['course']:<10}{float(r['grade']):>7.2f}")

if __name__ == "__main__":
    create_csv()
    display_csv()
