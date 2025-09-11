# 4.1 Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box.
# Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.

name = input("Enter your name: ")
print('Hello',name)

print('\n')

# 4.2 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number.


hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

grosspay = hours * rate
print(grosspay)