students = [{'name': 'Ann', 'grade': 92},
            {'name': 'Pavlo', 'grade': 85},
            {'name': 'Mark', 'grade': 95},
            {'name': 'Maria', 'grade': 78}]

reverse_sort = input("Сортувати від меншого до більшого? (так/ні): ").lower()

reverse = False
if reverse_sort == 'ні':
    reverse = True

sorted_by_name = sorted(students, key=lambda x: x['name'], reverse=reverse)
print("Сортування за ім'ям:")
for student in sorted_by_name:
    print(f"Name: {student['name']}, Grade: {student['grade']}")

sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=reverse)
print("Сортування за оцінкою:")
for student in sorted_by_grade:
    print(f"Name: {student['name']}, Grade: {student['grade']}")