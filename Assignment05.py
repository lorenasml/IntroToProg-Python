# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Lorena,11/09/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables

student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

# When the program starts, read the file data into a list of dictionary rows (table)
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines(): # Reads all the lines in a file and returns a list
        # Transform the data from the file
        student_data = row.split(',')
        student_data = {"student_first_name": student_data[0],
                        "student_last_name": student_data[1],
                        "course_name": (student_data[2].strip())}  # Load it into our collection (list of dictionary rows)
        students.append(student_data)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep="\n")
    print("Creating file...")
# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    # Prompt user to input menu choice
    menu_choice = input("Enter a menu option (1-4): ")

# Prompt user to input data
    if menu_choice == "1":
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Which course are you enrolled in? ")
            student_data = {"student_first_name": student_first_name,
                            "student_last_name": student_last_name,
                            "course_name": course_name}
            students.append(student_data)
            # print(students)
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e: #catch-all
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")

        continue

    # Present the current data
    elif menu_choice == "2":
        print("-"*50)
        print(students)
        print("-"*50)
        for student in students:
            print(f"{student["student_first_name"]}, {student["student_last_name"]}, {student["course_name"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                for student in students:
                    file.write(f"{student["student_first_name"]},{student["student_last_name"]},{student["course_name"]}\n")
            file.close()
        except KeyError as e:
            print("Please make sure your dictionary key exists!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e: #catch all
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep="\n")
        print("The following students have been successfully enrolled:")
        with open(FILE_NAME, "r") as file:
            for row in file:
                print(row.strip())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, or 3")

print("Exiting program")