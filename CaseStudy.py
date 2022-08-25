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
