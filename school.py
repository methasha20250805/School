"""
Simple School Management System

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


class Teacher(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.classes = []  # list of class names the teacher teaches

    def __str__(self):
        classes = ", ".join(self.classes) if self.classes else "None"
        return f"[{self.id}] {self.name} - Teaches: {classes}"


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.teacher = None  # Teacher object or None
        self.students = []  # list of Student objects

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "No teacher assigned"
        student_names = ", ".join(s.name for s in self.students) if self.students else "No students"
        return f"Class '{self.name}' | Teacher: {teacher_name} | Students: {student_names}"

class School:
    def __init__(self):
        self.students = {}   # id -> Student
        self.teachers = {}   # id -> Teacher
        self.classes = {}    # name -> ClassRoom
        self._next_student_id = 1
        self._next_teacher_id = 1

    # ---------- Add people ----------
    def add_student(self, name):
        student_id = f"S{self._next_student_id}"
        self._next_student_id += 1
        self.students[student_id] = Student(student_id, name)
        print(f"Added student '{name}' with ID {student_id}")

    def add_teacher(self, name):
        teacher_id = f"T{self._next_teacher_id}"
        self._next_teacher_id += 1
        self.teachers[teacher_id] = Teacher(teacher_id, name)
        print(f"Added teacher '{name}' with ID {teacher_id}")

    # ---------- Classes ----------
    def add_class(self, class_name):
        if class_name in self.classes:
            print(f"Class '{class_name}' already exists.")
            return
        self.classes[class_name] = ClassRoom(class_name)
        print(f"Created class '{class_name}'")

    def assign_teacher_to_class(self, teacher_id, class_name):
        teacher = self.teachers.get(teacher_id)
        classroom = self.classes.get(class_name)

        if not teacher:
            print(f"No teacher found with ID {teacher_id}")
            return
        if not classroom:
            print(f"No class found named '{class_name}'")
            return

        classroom.teacher = teacher
        if class_name not in teacher.classes:
            teacher.classes.append(class_name)
        print(f"Assigned {teacher.name} to teach '{class_name}'")

    def enroll_student_in_class(self, student_id, class_name):
        student = self.students.get(student_id)
        classroom = self.classes.get(class_name)

        if not student:
            print(f"No student found with ID {student_id}")
            return
        if not classroom:
            print(f"No class found named '{class_name}'")
            return

        if student not in classroom.students:
            classroom.students.append(student)
        if class_name not in student.classes:
            student.classes.append(class_name)
        print(f"Enrolled {student.name} in '{class_name}'")

        # ---------- Viewing ----------

    def list_students(self):
        if not self.students:
            print("No students yet.")
        for s in self.students.values():
            print(s)

    def list_teachers(self):
        if not self.teachers:
            print("No teachers yet.")
        for t in self.teachers.values():
            print(t)