"""
Dots Alignment Algorithm

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""
L = ["string", -12.3456, 100, "more Strings!", 212312.2222, -0.0, 5]
L1 = []
d = 0

# Removes Strings
for x in L:
    try:
        d = str(x)
        decimalPlace = d.find(".")
        if decimalPlace == -1:
            try:
                add = int(x)
                addd = str(add)
                L1.append(addd)
            except:
                print("String has been removed.")
        if decimalPlace > 0:
            add = float(x)
            addd = str(add)
            L1.append(addd)
    except:
        print("String has been removed")


# Align Dots
a = 0
for x in L1:
    decimalPlace = str(x).find(".")
    if decimalPlace > a:
        a = decimalPlace
    if decimalPlace == -1:
        if len(x) > a:
            a = len(x)

for x in L1:
    decimalPlace = str(x).find(".")
    print(decimalPlace)
    if decimalPlace == -1:
        spaces = a - len(x)
    else:
        spaces = a - decimalPlace
    print(spaces*" ", x)
