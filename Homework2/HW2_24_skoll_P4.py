"""
Homework 2
>Problem 4

Author: Derrick Unger
Date: 1/24/20
CSC232 Winter 2020
"""

# Initialize Variables
i = 0  # Array Counter
inputSum = 0

print("\n=======================================")
print("     Compound Interest Calculator\n")

print("Input instructions:")
print("     -Input interest rate in percent form i.e. input 10.5 for 10.5%")
print("     -When prompted, input one of these desired factors in this form: ")
print("     -F/P, P/F, P/A, A/P, A/F, F/A, A/G, or P/G\n")

while True:
    try:
        i = eval(input("Enter a desired interest rate: "))
        factorIn = input("Choose desired factor title: ")
        print("\n  n        ", factorIn)
        print(" ===     ==========")
        i = i/100

        # Equations
        for n in range(1, 11):
            FP = (1+i)**n
            PF = 1/FP
            PA = (((1+i)**n)-1)/(i*(1+i)**n)
            AP = 1/PA
            AF = i/((1+i)**n-1)
            FA = 1/AF
            AG = abs((1/i)-(n/(((1+i)**n)-1)))
            PG = abs((((1+i)**n)-(i*n)-1)/((i**2)*((1+i)**n)))

            if factorIn == "F/P":
                factor = str.format('{0:.4f}', FP)
            elif factorIn == "P/F":
                factor = str.format('{0:.4f}', PF)
            elif factorIn == "P/A":
                factor = str.format('{0:.4f}', PA)
            elif factorIn == "A/P":
                factor = str.format('{0:.4f}', AP)
            elif factorIn == "A/F":
                factor = str.format('{0:.4f}', AF)
            elif factorIn == "F/A":
                factor = str.format('{0:.4f}', FA)
            elif factorIn == "A/G":
                factor = str.format('{0:.4f}', AG)
            elif factorIn == "P/G":
                factor = str.format('{0:.4f}', PG)
            else:
                print("Invalid factor, try again")

            if n < 10:
                print(" ", n, "      ", factor)
            else:
                print("", n, "      ", factor)
        break

    except:
        print("Error: Invalid value, try again\n")

print("=======================================\n")
