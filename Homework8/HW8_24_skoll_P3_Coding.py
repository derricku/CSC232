"""
Homework 8
>Problem 3 Coding

Author: Derrick Unger
Date: 3/7/20
CSC232 Winter 2020
"""
# Write Original Message Here
outfile = open("Original.txt", "w")
outfile.write("The cake is a lie!")
outfile.close()


# Read in Original Message
f = open("Original.txt", "r")
mssg1, mssg2 = [], []
for line in f:
    mssg1 = list(line)


# Read in CodeBook
f = open("CodeBook.txt", "r")
code1, code2 = [], []

for line in f:
    line = line.strip()
    orig, scram = line.split()
    code1.append(orig)
    code2.append(scram)
f.close()


# Replace Original Chars with Scrambled Code
for char in mssg1:
    if char.upper() in code1:  # Filter out non alphabetical chars
        charloc = code1.index(char.upper())
        mssg2.append(code2[charloc])
    else:
        mssg2.append(char)


# Write to Coded File
outfile = open("SecretMessage.txt", "w")
outfile.write("".join(mssg2))
outfile.close()
