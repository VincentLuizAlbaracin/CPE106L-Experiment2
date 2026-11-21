''' Activity 2, Task 1: handling user input errors (grades).'''

def get_grade(prompt="Enter grade (0-100): "):
    while True:
        raw = input(prompt)
        try:
            grade = float(raw)
        except ValueError:
            print(f"  Error: '{raw}' is not a number. Please enter digits only.")
            continue
        if not 0 <= grade <= 100:
            print(f"  Error: {grade} is out of range. Grades must be 0 to 100.")
            continue
        return grade

def main():
    grades = [get_grade(f"Grade {i}: ") for i in range(1, 4)]
    print("Accepted grades:", grades)
    print(f"Average: {sum(grades)/len(grades):.2f}")

if __name__ == "__main__":
    main()
