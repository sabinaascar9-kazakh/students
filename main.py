students = ["Айгерим", "Нурлан", "Алина"]

def show_students():
    print("Список студентов:")
    for i, name in enumerate(students, 1):
        print(f"{i}. {name}")

show_students()