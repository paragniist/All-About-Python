# 5.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

if hours > 40:
    grosspay = (hours-40)*(rate*1.5)+ 40*rate
    print(grosspay)
else:
    grosspay =hours*rate
    print(grosspay)

    print('\n')

# 5.2 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = float(input('Enter score between 0.0 and 1.0'))

if score>1.0 and score<0.0:print('Out of range')
elif score>=0.9:print('A')
elif score>=0.8:print('B')
elif score>=0.7:print('C')
elif score>=0.6:print('D')
elif score<0.6 and score>=0.0:print('F')
elif score<0.0:print('Out of range')
else: print('Fail')
