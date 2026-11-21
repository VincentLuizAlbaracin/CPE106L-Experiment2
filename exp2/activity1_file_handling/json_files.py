''' Activity 1, Task 3: JSON file operations (students.json).'''
import json

FILENAME = "students.json"
DATA = {
    "school": "Sample University",
    "students": [
        {"id": "2021001", "name": "Juan Dela Cruz", "course": "BSCpE",
         "grades": [92, 90, 95]},
        {"id": "2021002", "name": "Maria Santos", "course": "BSCpE",
         "grades": [88, 85, 91]},
        {"id": "2021003", "name": "Jose Reyes", "course": "BSEE",
         "grades": [79, 82, 77]},
    ],
}

def create_json():
    with open(FILENAME, "w") as f:
        json.dump(DATA, f, indent=4)
    print(f"[Created] {FILENAME}")

def display_json():
    with open(FILENAME) as f:
        data = json.load(f)
    print("School:", data["school"])
    for s in data["students"]:
        avg = sum(s["grades"]) / len(s["grades"])
        print(f"  {s['id']} | {s['name']:<16} | {s['course']:<6} | "
              f"grades={s['grades']} | average={avg:.2f}")

if __name__ == "__main__":
    create_json()
    display_json()
