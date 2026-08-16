
# Simple School Management System
#  You can Add students
#  You can Add teachers
#  Create classes (subjects)
#  Assign a teacher to a class
#  Enroll a student in a class
#  View everything currently stored

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

    # Add people
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

    # Classes
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

 # Viewing

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

    def list_classes(self):
        if not self.classes:
            print("No classes yet.")
        for c in self.classes.values():
            print(c)

    #  CLI


MENU = """
School Management System
    1. Add student
    2. Add teacher
    3. Add class
    4. Assign teacher to class
  5. Enroll student in class
  6. View students
  7. View teachers
  8. View classes
  9. Exit
  Choose an option (1-9): """


def main():
    school = School()

    while True:
        choice = input(MENU).strip()

        if choice == "1":
            name = input("Student name: ").strip()
            school.add_student(name)

        elif choice == "2":
            name = input("Teacher name: ").strip()
            school.add_teacher(name)

        elif choice == "3":
            name = input("Class name: ").strip()
            school.add_class(name)

        elif choice == "4":
            school.list_teachers()
            teacher_id = input("Teacher ID: ").strip()
            school.list_classes()
            class_name = input("Class name: ").strip()
            school.assign_teacher_to_class(teacher_id, class_name)

        elif choice == "5":
            school.list_students()
            student_id = input("Student ID: ").strip()
            school.list_classes()
            class_name = input("Class name: ").strip()
            school.enroll_student_in_class(student_id, class_name)

        elif choice == "6":
            school.list_students()

        elif choice == "7":
            school.list_teachers()

        elif choice == "8":
            school.list_classes()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

    if __name__ == "__main__":
        main()