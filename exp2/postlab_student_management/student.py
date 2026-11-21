''' Student class for the Student Management System.'''

class Student:
    def __init__(self, student_id, name, course, grades=None):
        self.student_id = str(student_id)
        self.name = name
        self.course = course
        self.grades = list(grades) if grades else []

    def add_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def to_dict(self):
        return {"student_id": self.student_id, "name": self.name,
                "course": self.course, "grades": self.grades}

    @classmethod
    def from_dict(cls, d):
        return cls(d["student_id"], d["name"], d["course"], d.get("grades", []))

    def __str__(self):
        return (f"{self.student_id:<10}{self.name:<20}{self.course:<8}"
                f"{self.average():>7.2f}  {self.grades}")
