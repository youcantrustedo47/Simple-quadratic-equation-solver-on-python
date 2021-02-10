'''
Simple quadratic equation solver

by trustnoedo

this program will calculate the possible solutions of a quadratic equations in the form:
------------------------------- ax^2 + bx + c -------------------------------
'''

import math as m

# Function
def eq(a, b, c):

    choice = int(input("Choose an option:\n"
                       "1. Approximate to an integer\n"
                       "2. Give the real solution\n"
                       "\n"))
    d = float(b**2 - (4*(a*c)))

    if d < 0:
        print()
        print("There are no solutions for this equation!")
        print()
    elif d == 0:
        if choice == 1:
            s = int(-b / 2 * a)
            print("x = " + str(s))
        else:
            s = -b / 2 * a
            print("x = " + str(s))


    else:
        if choice == 1:
            sd = m.sqrt(d)
            x1 = int((-b + sd) / (2 * a))
            x2 = int((-b - sd) / (2 * a))
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))
        else:
            sd = m.sqrt(d)
            x1 = ((-b + sd) / (2 * a))
            x2 = ((-b - sd) / (2 * a))
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))

# Introduction
print()
print("------------------------------------------------")
print()
print("I can solve an equation with form: ax^2 + bx + c")
print()
print("------------------------------------------------")

# Storing
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Call
eq(a, b, c)
