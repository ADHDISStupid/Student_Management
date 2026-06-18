DB = []

def LOAD():
    try:
        with open("Student.txt", "r") as file:
            for line in file:
                DB.append(line.strip())
    except FileNotFoundError:
        pass



def SAVE():
    with open("Student.txt", "w") as file:
        for student in DB:
            file.write(student + "\n")


def add_student():
    add = input("Add Student: ")
    DB.append(add)
    print("Added Student:", add)
    SAVE()


def remove_student():
    remove = input("Remove Student: ")

    if remove in DB:
        DB.remove(remove)
        print("Removed Student:", remove)
        SAVE()
    else:
        print("Student not found.")


def view_student():
    if not DB:
        print("No students found.")
    else:
        for student in DB:
            print("-", student)


def search_student():
    search = input("Search Student: ")

    if search in DB:
        print("Found:", search)
    else:
        print("Not found.")


LOAD()

print("""
1. Add students
2. View students
3. Remove students
4. Search students
5. Exit
""")

while True:
    teacher = input("Enter option: ")

    match teacher:
        case '1':
            add_student()
        case '2':
            view_student()
        case '3':
            remove_student()
        case '4':
            search_student()
        case '5':
            break