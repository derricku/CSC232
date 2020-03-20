"""
Test 6
>Problem 1

Author: Derrick Unger
Date: 3/20/20
CSC232 Winter 2020
"""

print("\n" + "="*40)
print("PROBLEM 1")
print("Input format: last,first 123-45-6789 23.51")
print("Notice, no space between first and last as shown in problem statement")
print("To exit, enter 'exit  ' without quotes and with two spaces at end")

names = []
socs = []
miles = []
while True:
    try:
        name, soc, mile = input("\nInput values: ").split(" ")

        # Exit Checks
        if (name.upper() == "EXIT" or soc.upper() == "EXIT" or
           mile.upper() == "EXIT"):
            print("Exit detected... quitting\n")
            break

        names.append(name)
        socs.append(soc)
        miles.append(mile)
        print(names, socs, miles)

    except:
        print("\nError: Invalid input, retry\n")

# ALIGNMENT
a, b, c = 0, 0, 0
for y in names:
    commaPlace = str(y).find(",")
    if commaPlace > b:
        b = commaPlace

    # Max Len after Comma
    if (len(y) - commaPlace) > c:
        c = len(y) - commaPlace

for x in miles:
    decimalPlace = str(x).find(".")
    if decimalPlace > a:
        a = decimalPlace
    if decimalPlace == -1:
        if len(x) > a:
            a = len(x)

for x in range(len(names)):
    # Sort Commas
    commaPlace = str(names[x]).find(",")
    if commaPlace == -1:
        spaces = b - len(name[x])
    else:
        spaces = b - commaPlace

    # Sort Decimals
    decimalPlace = str(miles[x]).find(".")
    if decimalPlace == -1:
        spaces2 = a - len(miles[x])
    else:
        spaces2 = a - decimalPlace

    # Gap
    firstLen = len(names[x]) - commaPlace
    gap = c - firstLen + 1

    # Print with Spacing
    print(spaces*" " + names[x] + gap*" " + socs[x] + " " + spaces2*" " + miles[x])

print("\n" + "="*40)
