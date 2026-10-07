students = ["Айгерим", "Нурлан", "Алина"]

def show_students():
    print("=" * 30)
    print("Список всех студентов:")
    print("=" * 30)
    for i, name in enumerate(students, 1):
        print(f"{i}. {name}")
    print("=" * 30)

def find_student(name):
    if name in students:
        print(f"Найден студент: {name}")
    else:
        print(f"Студент '{name}' не найден")

def add_student(name):
    students.append(name)
    print(f"Студент {name} успешно добавлен")

show_students()
print("\n--- Поиск ---")
find_student("Нурлан")
print("\n--- Добавление ---")
add_student("Данияр")
show_students()