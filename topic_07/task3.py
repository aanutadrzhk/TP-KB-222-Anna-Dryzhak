class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Anna", 18),
    Student("Bob", 22),
    Student("Pavlo", 20),
    Student("David", 21)
]

sorted_students = sorted(students, key=lambda x: x.age)

for student in sorted_students:
    print(f"Name: {student.name}, Age: {student.age}")