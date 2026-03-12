# 1. Write a simple program that reads two integer numbers from the keyboard
# and then divides one by the other using integer division and then reports the result.
# Note you should store both inputs into variables and confirm that the second number (i.e. the divisor) is not zero;
# this confirmation should be done before actually performing the division,
# as division by 0 is not mathematically defined and will cause your program to crash.
# You should also store the result of the integer division in a variable and print it out.

x = int(input("Enter 1st numnber: "))
y = int(input("Enter 2nd number: "))

if y==0:
         print("Error: Execution not possible")
else:
         D = x//y
         print(D)