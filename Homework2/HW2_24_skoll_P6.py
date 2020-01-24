"""
Homework 2
>Problem 6

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

# Initialize Variables
gpa, gpaCumulative, gpaAverage = 0, 0, 0
i, s = 1, 0

print("\n=======================================")
print("     GPA Calculator\n")

while True:
    try:
        s = int(input("Enter number of students: "))
        while i <= s:
            print("Enter student", i, "'s grade [A B C D]: ", end="")
            gradeInput = input()
            if gradeInput == "A":
                gpa = 4.0
                i += 1
                gpaCumulative += gpa
            elif gradeInput == "B":
                gpa = 3.0
                i += 1
                gpaCumulative += gpa
            elif gradeInput == "C":
                gpa = 2.0
                i += 1
                gpaCumulative += gpa
            elif gradeInput == "D":
                gpa = 1.0
                i += 1
                gpaCumulative += gpa
            else:
                print("Invalid grade. Enter that student's grade again.")
        break

    except:
        print("\nError: Invalid value, try again\n")

averageGpa = gpaCumulative/s
print("\nAverage GPA of", s, "students is: ", averageGpa, "\n")
print("=======================================\n")
