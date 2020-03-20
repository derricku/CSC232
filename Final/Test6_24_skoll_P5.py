"""
Test 6
>Problem 5

Author: Derrick Unger
Date: 3/20/20
CSC232 Winter 2020
"""
print("\n" + "="*40)
print("PROBLEM 5\n")

# Read in Original Message
f = open("incoming.txt", "r")
mssg1 = []
for line in f:
    line = line.strip()  # Remove trailing and leading whitespace from orig
    if line != "END":  # Skip last line
        lines = line.split(" ")
        mssg1.append(lines)


# Read in Morse CodeBook
f = open("NewMorseCode.txt", "r")
code1, code2 = [], []

for line in f:
    line = line.strip()
    if line != "END":  # Skip last line
        orig, scram = line.split(" ")
        code1.append(orig)
        code2.append(scram)
f.close()


# Replace Morse with Alphanumeric Values
mssg2 = []  # List of Translated Lines
for line in mssg1:  # Iterate thorugh each line of mssg1
    print("Original: ", " ".join(line))
    line2 = []  # List of Translated values in line, reset each line
    for x in range(len(line)):  # Iterate each value in line
        if line[x] in code2:  # Make sure in codebook
            charloc = code2.index(line[x])  # Location of value in codebook

            # Implemented code shift
            if charloc == len(code1)-1:  # Loop back to beginning if last
                line2.append(code1[0])
            else:
                line2.append(code1[charloc + 1])

        else:
            print("Invalid Morse Code Input")
            mssg2 = []  # Clear text
            mssg2.append("Invalid Morse Code Input")  # Replace with error
            break
    mssg2.append(" ".join(line2))  # Join values in line, store in mssg2
    print("Translated: ", mssg2[mssg1.index(line)])
    # Write to Coded File
    outfile = open("Output.txt", "w")
    outfile.write("\n".join(mssg2))
    outfile.close()

print("="*40)
