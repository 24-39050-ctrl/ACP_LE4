import os

doc_path = os.path.expanduser("D:/codes")
if not os.path.exists(doc_path):
    os.makedirs(doc_path)


while True:

    print("\n=======Main Menu=======\n" +
          "1. Register Student\n" +
          "2. Open Student Record\n" +
          "3. Exit")

    try:
        userinput = int(input("Enter your choice: "))
        if userinput == 1:
            print("\n====Student Registration====")
            studentno = int(input("Student No: "))
            lastname = input("Last Name: ")
            firstname = input("First Name: ")
            middleinitial = input("Middle Initial: ")
            program = input("Program: ")
            age = input("Age: ")
            gender = input("Gender: ")
            birthday = input("Birthday MM/DD/YYYY: ")
            contactno = input("Contact Number: ")

            data = [
                f"Student No.: {studentno}",
                f"Full Name: {lastname.capitalize()}, {firstname.capitalize()} {middleinitial.capitalize()}.",
                f"Program: {program.upper()}",
                f"Age: {age}",
                f"Gender: {gender.capitalize()}",
                f"Birthday: {birthday}",
                f"Contact No.: {contactno}"
            ]

            file_path = os.path.join(doc_path, f"{studentno}.txt")
            with open(file_path, "w") as f:
                for line in data:
                    f.write(line + "\n")

            print(f"Student record saved to {file_path}")

        elif userinput == 2:
            print("\n=======Open Student Record=======")
            student_no = input("Enter Student No: ")
            file_path = os.path.join(doc_path, f"{student_no}.txt")
            try:
                with open(file_path, "r") as f:
                    print("\n=======Student Record=======")
                    for line in f:
                        print(line.strip())
            except FileNotFoundError:
                print("Error: Student record not found.")

        elif userinput == 3:
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
