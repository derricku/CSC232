"""
Homework 9
>Problem 3

Author: Derrick Unger
Date: 3/14/20
CSC232 Winter 2020
"""
# Write Original Message Here
outfile = open("Original.txt", "w")
outfile.write("... --- ...")
outfile.close()


# Read in Original Message
f = open("Original.txt", "r")
mssg1 = []
for line in f:
    line = line.strip()  # Remove trailing and leading whitespace from original
    mssg1 = line.split(" ")

# Read in Morse CodeBook
f = open("MorseCode.txt", "r")
code1, code2 = [], []

for line in f:
    line = line.strip()
    orig, scram = line.split(" ")
    code1.append(orig)
    code2.append(scram)
f.close()


# Replace Morse with Alphanumeric Values
mssg2 = []
x = 0
while x < len(mssg1):
    if mssg1[x] in code2:
        charloc = code2.index(mssg1[x])
        mssg2.append(code1[charloc])
        x += 1
    else:
        print("Invalid Morse Code Input")
        mssg2 = []  # Clear text
        mssg2.append("Invalid Morse Code Input")  # Replace with error
        break

# Write to Coded File
outfile = open("Output.txt", "w")
outfile.write("".join(mssg2))
outfile.close()
