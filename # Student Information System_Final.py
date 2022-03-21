# Student Insormation System
import tkinter
import csv
import getpass
#variables
Student_Data = ['Id no.', 'name', 'Year', 'Gender', 'Course']
student_database = 'student.csv'
Register = 'register.csv'

def display_menu():
    print("-----------------------------Student Information System---------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update/Edit Student")
    print("5. Delete Student")
    print("6. Quit")
    
def add_student():
    print("---------------------------------Add Student Information----------------------------------")
    global Student_Data
    global student_database

    student_data = []
    for Data in Student_Data:
        value = input("Enter " + Data + ": ")
        student_data.append(value)

    with open(student_database, "a") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return

def view_students():
    global Student_Data
    global student_database

    print("-----------------------Student Records--------------------")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for Data in Student_Data:
            print(Data, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global Student_Data
    global student_database

    print("-----------------Search Student--------------")
    ID = input("Enter ID no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    print("----------------------Student Found-------------------------")
                    print("ID No.: ", row[0])
                    print("Name: ", row[1])
                    print("Year: ", row[2])
                    print("Gender: ", row[3])
                    print("Course: ", row[4])
                    break
        else:
            print("ID No. not found in our database")
    input("Press any key to continue")


def update_student():
    global Student_Data
    global student_database

    print("-----------------------Update/Edit Student----------------")
    ID = input("Enter ID no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in Student_Data:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ID No. not found in our database")

    input("Press any key to continue")


def delete_student():
    global Student_Data
    global student_database
    print("--------------------------Delete Student----------------------")
    ID = input("Enter ID no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID no. ", ID, "deleted successfully")
    else:
        print("ID No. not found in our database")
    input("Press any key to continue")

def register():
    with open('register.csv',mode="a" , newline="") as f:
        writer=csv.writer(f,delimiter=",")

        email=input("--------------------------\nPlease enter your email:")
        password=input("--------------------------\nPlease enter your Password:")
        password2=input("--------------------------\nPlease Re-enter password:")

        if password==password2:
            writer.writerow([email, password])
            print("Registration Complete")
        else:
            print("Try again")
def login():
    email=input("-------------------\nPlease Enter Email:")
    password=input("-------------------------------\nPlease Enter Password:")
    with open("Register.csv", mode="r")as f:
        reader=csv.reader(f,delimiter= ",")
        for row in reader:
            if row == [email,password]:
                print("-----------------")
                print("You are Logged in")
                print("-----------------")
                return True
    print("---------------------------------")
    print("Username/Password not recognized")
    print("--------------------------------")
    exit()
    
while True:
    Register=input("Are you Already Registered?(Y/N):")
    if Register=="N":
        register()
    elif Register=="Y":
        login()
    while True:
        display_menu()

        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            exit()
        else:
            print("---------------------------------------")
            print ("Something Went Wrong, Please Try Again")
            print("------------------------------------")
            exit()
