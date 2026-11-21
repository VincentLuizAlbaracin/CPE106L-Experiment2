''' Activity 3, Task 2: import and use Utilities.py.'''
import Utilities

grades = [92, 88, 95]
avg = Utilities.average(grades)
print("Average calculator :", round(avg, 2))
print("Grade evaluator    :", Utilities.evaluate_grade(avg))
print("Student display    :")
Utilities.display_student("2021001", "Juan Dela Cruz", "BSCpE", grades)
try:
    Utilities.average([])
except ValueError as e:
    print("Caught:", e)
