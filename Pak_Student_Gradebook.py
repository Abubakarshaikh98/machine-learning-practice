def add_student(record):
    name = input("Student's Name: ")
    roll_no =input("Roll No: ")

    if roll_no in record:
        print("Roll Number already exists! Try again.\n")
        return
    
    marks =[]
    subjects = ["English","Urdu","Math"]

    for subject in subjects:
        while True:
            try:
                m =int(input(f"{subject} marks (0-100): "))

                if 0 <= m<= 100:
                    marks.append(m)
                    break
                else:
                    print("Marks Must be between 0 and 100. Try again ")
            except ValueError:
                print("Invalid Input ! Please Enter a Number")   
    record[roll_no] = {"Name":name,"Marks":marks}
    print("Student Added succesfully! \n")

def view_Gradebook(record):
    if not record:
        print("No Students yet. \n")
        return
    print("\n ========= Grade Book =========")
    for roll_no, data in record.items():
        avg = sum(data["Marks"]) / len(data["Marks"])
        grade = (
    "A" if avg >= 80 else
    "B" if avg >= 70 else
    "C" if avg >= 60 else
    "D" if avg >= 50 else
    "F"
)
        print(f"Roll_No: {roll_no}")
        print(f"Name: {data['Name']}")
        print(f"Average: {avg:.1f}")
        print(f"Grade: {grade}")

        print("===========================")
    print()

def main():
    record = {}
    print("Pakistan Students Grade Book.\n")

    while True:
        print("1. Add Student")
        print("2. View Grade Book")
        print("3. Exit")
        ch = input("Chose an option: ")

        if ch == "1":
            add_student(record)
        elif ch == "2":
            view_Gradebook(record)
        elif ch == "3":
            print("Allah Hafiz")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()
