''' Helper functions: validated input and report formatting.'''

def get_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty.")

def get_grade(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            grade = float(raw)
        except ValueError:
            print(f"  '{raw}' is not a number.")
            continue
        if 0 <= grade <= 100:
            return grade
        print("  Grade must be between 0 and 100.")

def get_grades(prompt="Grades (comma-separated, blank for none): "):
    while True:
        raw = input(prompt).strip()
        if not raw:
            return []
        try:
            grades = [float(g) for g in raw.split(",")]
        except ValueError:
            print("  Use numbers separated by commas, e.g. 90, 85.5, 78")
            continue
        if all(0 <= g <= 100 for g in grades):
            return grades
        print("  Every grade must be between 0 and 100.")

def get_menu_choice(low, high):
    while True:
        raw = input("Choose an option: ").strip()
        if raw.isdigit() and low <= int(raw) <= high:
            return int(raw)
        print(f"  Enter a number from {low} to {high}.")

def letter_grade(avg):
    for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if avg >= cutoff:
            return letter
    return "F"

HEADER = f"{'ID':<10}{'Name':<20}{'Course':<8}{'Avg':>7}  Grades"
