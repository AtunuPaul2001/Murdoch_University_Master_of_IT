# 5. Modify Exercise 5 in Lab 1 using a while loop:
# the program will repeatedly read a user input as the temperature value in Fahreinheit, and convert it to Celsius
# and print it out, until the user input is "end".

temp = input ("Enter Fahrenheit (Or End to quit): ")

while temp != "end":
    fahrenheit = float(temp)
    celsius = ((fahrenheit-32)*5) / 9
    print("Fahrenheit", fahrenheit)
    print ("Celsius", celsius)
    temp = input("Enter Fahrenheit (Or End to quit): ")

print("End")