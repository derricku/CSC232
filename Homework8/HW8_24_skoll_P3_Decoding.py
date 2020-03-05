"""
Homework 8
>Problem 3 Decoding

Author: Derrick Unger
Date: 3/7/20
CSC232 Winter 2020
"""
# Read in Coded Message
f = open("SecretMessage.txt", "r")
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


# Replace Scrambled Chars with Correct Chars
for char in mssg1:
    if char.upper() in code2:  # Filter out non alphabetical chars
        charloc = code2.index(char.upper())
        mssg2.append(code1[charloc])
    else:
        mssg2.append(char)


# Write to Coded File
outfile = open("Translated.txt", "w")
outfile.write("".join(mssg2))
outfile.close()
