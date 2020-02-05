"""
Homework 4
>Problem 5

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

allInfo = []
code = 0

while True:
    try:
        while code == 0:
            sep = input("\nEnter how you would like to separate your input: ")
            print("When ready to stop, type exit in the first category.\n")
            if sep == ".":
                print("Seperator can't be . because of floats, try again")
                code = 0
            else:
                code = 1

        city, temp, feel = input("\nEnter the city, average temperature, and \
how it felt separated by the separator you choice: ").split(sep)

        # Error and Exit Checks
        if city.upper() == "EXIT":
            break
        elif city.isnumeric() or feel.isnumeric():
            err = 1/0
        elif city.strip() is None:
            err = 1/0
        else:
            temp = eval(temp)

            # Input Storage
            info = [city, str.format('{0:.2f}', temp), feel]
            allInfo.append(info)

    except:
        print("Invalid input, try again.")

# Dots Alignment Alg.
maxCityLen = maxTempLen = maxFeelLen = 0
cityLen = []
tempLen = []

for x in allInfo:
    cLen = len(str(x[0]))       # City Length Handler
    cityLen.append(cLen)
    if cLen > maxCityLen:
        maxCityLen = cLen

    tLen = len(str(x[1]))       # Temp Length Handler
    tempLen.append(tLen)
    if tLen > maxTempLen:
        maxTempLen = tLen

    fLen = len(str(x[2]))       # Feel Length Handler
    if fLen > maxFeelLen:
        maxFeelLen = fLen

# Title Alginment and Print
print("\n")
cTitle = "City"
tTitle = "Temperature"
fTitle = "Feeling"

print(cTitle+" "*(maxCityLen-len(cTitle)) + "   " +
      tTitle+" "*(maxTempLen-len(tTitle)) + "   " +
      fTitle+" "*(maxFeelLen-len(fTitle)))

print(("="*len(cTitle))+" "*(maxCityLen-len(cTitle)) + "   " +
      ("="*len(tTitle))+" "*(maxTempLen-len(tTitle)) + "   " +
      ("="*len(fTitle))+" "*(maxFeelLen-len(fTitle)))

# Info Alginment and Print
row = 0
while row < len(allInfo):
    cPrint = str(allInfo[row][0])+" "*(maxCityLen-cityLen[row])
    tPrint = str(allInfo[row][1])+" "*(maxTempLen-tempLen[row])
    fPrint = str(allInfo[row][2])
    print(cPrint, "   ", tPrint, "   ", fPrint)
    row += 1
