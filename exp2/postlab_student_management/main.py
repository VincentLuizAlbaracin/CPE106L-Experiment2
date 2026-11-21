''' Enhanced Student Management System - program execution.'''
import file_manager
import utilities as util
from student import Student

MENU = """
===== Student Management System =====
1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. Display All Students
6. Compute Average Grade (one student / class)
7. Generate Summary Report
8. Save Records
9. Load Records
0. Save and Exit
"""

def add_student(students):
    sid = util.get_text("Student ID: ")
    if sid in students:
        print("  That ID already exists.")
        return
    students[sid] = Student(sid, util.get_text("Name: "),
                            util.get_text("Course: "), util.get_grades())
    print("  Student added.")

def update_student(students):
    s = students.get(util.get_text("ID to update: "))
    if not s:
        print("  Student not found.")
        return
    name = input(f"New name [{s.name}]: ").strip()
    course = input(f"New course [{s.course}]: ").strip()
    if name: s.name = name
    if course: s.course = course
    if input("Replace grades? (y/n): ").strip().lower() == "y":
        s.grades = util.get_grades()
    print("  Student updated.")

def delete_student(students):
    sid = util.get_text("ID to delete: ")
    if students.pop(sid, None):
        print("  Student deleted.")
    else:
        print("  Student not found.")

def search_student(students):
    term = util.get_text("Search by ID or name: ").lower()
    found = [s for s in students.values()
             if term == s.student_id.lower() or term in s.name.lower()]
    if not found:
        print("  No matches.")
        return
    print(util.HEADER)
    for s in found:
        print(s)

def display_all(students):
    if not students:
        print("  No records.")
        return
    print(util.HEADER)
    for s in students.values():
        print(s)

def compute_average(students):
    if not students:
        print("  No records.")
        return
    sid = input("ID (blank for whole class): ").strip()
    if sid:
        s = students.get(sid)
        print(f"  {s.name}: {s.average():.2f}" if s else "  Student not found.")
    else:
        avgs = [s.average() for s in students.values() if s.grades]
        print(f"  Class average: {sum(avgs)/len(avgs):.2f}" if avgs
              else "  No grades recorded yet.")

def summary_report(students):
    graded = [s for s in students.values() if s.grades]
    print("\n--- SUMMARY REPORT ---")
    print(f"Total students : {len(students)}")
    if not graded:
        print("No grades recorded yet.")
        return
    avgs = [s.average() for s in graded]
    top = max(graded, key=Student.average)
    low = min(graded, key=Student.average)
    print(f"Class average  : {sum(avgs)/len(avgs):.2f}")
    print(f"Highest        : {top.name} ({top.average():.2f})")
    print(f"Lowest         : {low.name} ({low.average():.2f})")
    for s in students.values():
        print(f"  {s.name:<20}{s.average():>7.2f}  {util.letter_grade(s.average())}")

def main():
    students = file_manager.load_students()          # auto-load on startup
    print(f"Loaded {len(students)} record(s).")
    actions = {1: add_student, 2: update_student, 3: delete_student,
               4: search_student, 5: display_all, 6: compute_average,
               7: summary_report}
    while True:
        print(MENU)
        try:
            choice = util.get_menu_choice(0, 9)
            if choice == 0:
                break
            elif choice == 8:
                if file_manager.save_students(students):
                    print("  Records saved.")
            elif choice == 9:
                students = file_manager.load_students()
                print(f"  Loaded {len(students)} record(s).")
            else:
                actions[choice](students)
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted - saving and exiting.")
            break
        except Exception as e:                       # runtime errors handled gracefully
            print(f"  Something went wrong: {type(e).__name__}: {e}")
    file_manager.save_students(students)             # save before exit
    print("Records saved. Goodbye!")

if __name__ == "__main__":
    main()
