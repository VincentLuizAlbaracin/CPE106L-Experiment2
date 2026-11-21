''' Activity 3, Task 1: reusable utility module.'''

def average(numbers):
    ''' Return the mean of a list of numbers.'''
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)

def evaluate_grade(avg):
    ''' Return a letter grade for a 0-100 average.'''
    if not 0 <= avg <= 100:
        raise ValueError("Average must be between 0 and 100")
    for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if avg >= cutoff:
            return letter
    return "F"

def display_student(student_id, name, course, grades):
    ''' Print a student's information with average and letter grade.'''
    avg = average(grades)
    print(f"ID: {student_id} | Name: {name} | Course: {course}")
    print(f"Grades: {grades} | Average: {avg:.2f} | Grade: {evaluate_grade(avg)}")
