import csv
import os

FILE_NAME = "students.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name","Subject1","Subject2","Subject3"])

def menu():
    print("\n--- Student Record Manager ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Analyze Results")
    print("4. Exit")

def add_student():
    name = input("Enter Student Name: ")
    s1 = int(input("Enter marks in subject1: "))
    s2 = int(input("Enter marks in subject2: "))
    s3 = int(input("Enter marks in subject3: "))

    with open(FILE_NAME,"a",newline="")as file:
        writer = csv.writer(file)
        writer.writerow([name,s1,s2,s3])

    print(f"{name} added successfully!")

def display_students():
    if not os.path.exists(FILE_NAME):
        print("No Student Data Found.")
        return
    
    with open(FILE_NAME,"r")as file:
        reader = csv.reader(file)
        print("\n--- Student List ---")
        for i, row in enumerate(reader):
            if i == 0:
                print(f"{row[0]:<15}{row[1]:<10}{row[2]:<10}{row[3]:<10}")
                print("-"*45)
            else:
                print(f"{row[0]:<15}{row[1]:<10}{row[2]:<10}{row[3]:<10}")

def analyze_results():
    if not os.path.exists(FILE_NAME):
        print("No student data found.")
        return  

    total_avg = 0
    count = 0
    pass_count = 0
    fail_count = 0
    topper_name = ""
    topper_avg = -1

    with open(FILE_NAME,"r")as file:
        reader = csv.reader(file)
        next(reader)
        print("\n--- Student Analysis ---")
        print(f"{'Name':<15}{'Average':<10}{'Result':<10}")
        print("-"*35)

        for row in reader:
            name = row[0]
            marks = list(map(int,row[1:4]))
            avg = sum(marks)/3
            total_avg += avg
            count += 1

            if avg >= 50:
                result = "pass"
                pass_count += 1
            else:
                result = "Fail"
                fail_count += 1
            
            if avg > topper_avg:
                topper_avg = avg
                topper_name = name
            print(f"{name:<15}{avg:<10.2f}{result:<10}")

    if count > 0:
        print("-"*35)
        print(f"Class Average: {total_avg/count:.2f}")
        print(f"Topper: {topper_name}({topper_avg:.2f})")
        print(f"Pass students: {pass_count}")
        print(f"Fail Students: {fail_count}")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            analyze_results()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("invalid choice. try again.")

if __name__ == "__main__":
    main()