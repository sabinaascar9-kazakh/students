students = ["Айгерим", "Нурлан", "Алина"]

def show_students():
    print("=" * 30)
    print("Список всех студентов:")
    print("=" * 30)
    for i, name in enumerate(students, 1):
        print(f"{i}. {name}")
    print("=" * 30)

show_students()