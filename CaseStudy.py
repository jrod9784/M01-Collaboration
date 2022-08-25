# Jordan Luers
# Dean's list checker
# This app will accept student input for last name and first name, then accept input for their gpa. Then tell the student if they made the dean's list, Honor Roll, or nothing at all

studentLastName = input("Enter last name or 'ZZZ' to exit.")
studentFirstName = ""
GPA = 0.0
while studentLastName != "ZZZ" or studentLastName != "zzz":
    studentFirstName = input("Enter first name.")
    GPA = input("Enter your GPA as a decimal. (ex: 2.0).")
    if float(GPA) >= 3.5:
        print(studentFirstName + " " + studentLastName + " made the Dean's list!")
    elif float(GPA) >= 3.25:
        print(studentFirstName + " " + studentLastName +
              " made the Honor Roll!")
    else:
        print("Sorry " + studentFirstName + " " + studentLastName +
              ", you didn't make the dean's list or honor roll.")
    studentLastName = input("Enter last name or 'ZZZ' to exit.")
