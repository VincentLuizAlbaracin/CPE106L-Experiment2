''' JSON file read/write functions.'''
import json
import os
from student import Student

DEFAULT_FILE = "students.json"

def save_students(students, filename=DEFAULT_FILE):
    ''' Write {id: Student} to a JSON file. Returns True on success.'''
    try:
        with open(filename, "w") as f:
            json.dump([s.to_dict() for s in students.values()], f, indent=4)
        return True
    except OSError as e:
        print(f"Could not save records: {e}")
        return False

def load_students(filename=DEFAULT_FILE):
    ''' Read students from JSON. Missing/corrupt files give an empty dict.'''
    try:
        with open(filename) as f:
            records = json.load(f)
        return {d["student_id"]: Student.from_dict(d) for d in records}
    except FileNotFoundError:
        print(f"No '{filename}' found - starting with an empty record list.")
    except (json.JSONDecodeError, KeyError, TypeError):
        backup = filename + ".bak"
        try:
            os.replace(filename, backup)       # keep the bad file instead of overwriting it on exit
            print(f"'{filename}' is damaged or in the wrong format - kept as '{backup}', starting empty.")
        except OSError:
            print(f"'{filename}' is damaged or in the wrong format - starting empty.")
    return {}
