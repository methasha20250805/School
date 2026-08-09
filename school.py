"""
Simple School Management System
--------------------------------
Lets you:
  - Add students
  - Add teachers
  - Create classes (subjects)
  - Assign a teacher to a class
  - Enroll a student in a class
  - View everything currently stored

All data lives in memory (Python dictionaries/lists) while the
program is running. Data resets each time you restart the program.
"""
class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name


class Student(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.classes = []  # list of class names the student is enrolled in

    def __str__(self):
        classes = ", ".join(self.classes) if self.classes else "None"
        return f"[{self.id}] {self.name} - Enrolled in: {classes}"