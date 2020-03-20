"""
Test 6
>Problem 3

Author: Derrick Unger
Date: 3/20/20
CSC232 Winter 2020
"""

from datetime import datetime

print("\n" + "="*40)
print("PROBLEM 3")

format = "%H:%M:%S"
while True:
    try:
        # Input Time
        BEG_TIME = input("Input BEG_TIME in 00:00:00 format: ")
        END_TIME = input("Input END_TIME in 00:00:00 format: ")

        # Convert Times to Date Time Objects
        BEG1 = datetime.strptime(BEG_TIME, format)  # Start Time
        END1 = datetime.strptime(END_TIME, format)  # End Time
        # ------------------------------------------------------- Block2Compare

        # Read in Times Text File
        f = open("Candidates_Set1.txt", "r")
        cands = []
        BEG2 = []
        END2 = []
        NAME = []
        for line in f:
            line = line.strip()  # Remove trailing and leading whitespace
            line = " ".join(line.split())  # remove extra spaces
            cands = line.split(" ")

            if len(cands) > 1:  # Skip last line
                NAME.append(cands[0])
                BEG2.append(datetime.strptime(cands[1], format))
                END2.append(datetime.strptime(cands[2], format))
        break

    except:
        print("Error, incorrect input...")

print("\n")
for x in range(len(BEG2)):
    if BEG1 < END2[x] and BEG2[x] < END1:  # Check for Overlap
        print("Qualified Candidate: ", NAME[x])
        # Check Overlap Length
        if BEG1 < BEG2[x]:
            if END1 < END2[x]:
                howLong = END1 - BEG2[x]  # Overlap Type 1
            else:
                howLong = END2[x] - BEG2[x]  # Overlap Type 2
        elif BEG2[x] < BEG1:
            if END1 < END2[x]:
                howLong = END1 - BEG1  # Overlap Type 3
            else:
                howLong = END2[x] - BEG1  # Overlap Type 4

        print("Available for: ", howLong, "\n")
print("="*40)
