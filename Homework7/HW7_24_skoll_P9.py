"""
Homework 7
>Problem 9

Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""
# Read in numbers
f = open("NUMBERS.csv", "r")
nums = []
for line in f:
    line = line.strip()
    nums.append(float(line))
f.close()  # Close .csv


# Bubble Sorting
arr = nums  # Define your array here
n = len(nums)  # Define length of array here

# Traverse through all array elements
for i in range(len(nums)):

    # Last i elements are already in place
    for j in range(0, n-i-1):

        # Traverse the array from 0 to n-i-1
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# Align Dots and Write to .txt File
f = open("NUMBERSsortASC.txt", "w")
a = 0
b = 0
for x in arr:
    decPlace = str(x).find(".")
    if decPlace > a:
        a = decPlace
    if decPlace == -1:
        if len(x) > a:
            a = len(x)
c = 0

for x in arr:
    decPlace = str(x).find(".")
    if decPlace == -1:
        spaces = a - len(x)
    else:
        spaces = a - decPlace
    b = [spaces*" ", str(x)]
    b = "".join(b)
    print(b)
    f.write(b)  # Write line in .txt
    f.write("\n")  # Move to next line in .txt
f.close()
