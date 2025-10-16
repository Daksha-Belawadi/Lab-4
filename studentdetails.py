def write_student_info():
    name = input("Enter student name: ")
    usn = input("Enter student USN: ")
    division = input("Enter student division: ")

    with open("students.txt", "a") as file:
        file.write(f"Name: {name}, USN: {usn}, Division: {division}\n")

    print("Student information saved successfully!")

write_student_info()