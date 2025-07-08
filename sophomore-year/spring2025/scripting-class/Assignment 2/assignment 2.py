#Assignment 2 - More Input/Output

"""
Alright now we are stepping it up a bit in working with user input/output. 
Write a program that does the following things, 
Ask the user for their full name, student ID number and expected graduation year. 
Ask them how many classes currently this semester they are taking worth 1 credit hour and store the number.  (Known as num1)
Ask them how many classes currently this semester they are taking worth 2 credit hours and store the number. (Known as num2)
Ask them how many classes currently this semester they are taking worth 3 credit hour and store the number. (Known as num3)
Ask them how many classes currently this semester they are taking worth 4 credit hour and store the number. (Known as num4)
Use this math problem on the numbers entered: num1 + (2 x num2) + (3 x num3) + (4 x num4)
Store it into a variable called "creditHours"
Finally return the info to the user in  a similar fashion:
"Your name is (name) with the ID number of (ID number and expect to graduate in the year (year).
You are currently enrolled in (creditHours) credit hours this semester. Nice Job!"
"""

fullName = input("Enter your full name: ")
studentID = input("What is your student ID?: ")
gradYear = input("What year will you graduate?: ")

num1 = input("This semester, how many classes are you taking you take that are 1 credit hour?: ") 
num2 = input("This semester, how many classes are you taking you take that are 2 credit hours?: ")
num3 = input("This semester, how many classes are you taking you take that are 3 credit hours?: ")
num4 = input("This semester, how many classes are you taking you take that are 4 credit hours?: ")

creditHours = int(num1) + (2 * int(num2)) + (3 * int(num3)) + (4 * int(num4))
int(creditHours)

print("Hello " + fullName + ", your student ID is " + studentID + " and you will graduate in " + gradYear + ".")

if creditHours > 12:
    print("You are taking " + str(creditHours) + " credit hours this semester, you're doing great! Keep it up!")
elif creditHours < 9:
    print("You are taking " + str(creditHours) + " credit hours this semester, you could do better than that! :(")
else:
    print("You are taking " + str(creditHours) + " credit hours this semester, you're doing okay.")
