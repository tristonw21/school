#assignment3.py #Looping it all up
"""
Take the code you made for Python 2 and put it into a loop that repeats until the user says they want to end the program.
"""


def creditHourCalculate(): # Function to calculate credit hours
    while True:
        try:
            num1 = int(input("How many 1-credit hour classes are you taking?: "))
            num2 = int(input("How many 2-credit hour classes are you taking?: "))
            num3 = int(input("How many 3-credit hour classes are you taking?: "))
            num4 = int(input("How many 4-credit hour classes are you taking?: "))
            break  # Exit loop if all inputs are valid
        except ValueError:
            print("Invalid input! Please enter only whole numbers.")

    creditHours = num1 + (2 * num2) + (3 * num3) + (4 * num4)

    if creditHours > 12:
        print(f"\nYou are taking {creditHours} credit hours this semester. You're doing great! Keep it up!")
    elif creditHours < 9:
        print(f"\nYou are taking {creditHours} credit hours this semester. You could do better than that!")
    else:
        print(f"\nYou are taking {creditHours} credit hours this semester. You're doing okay.")


while True: # Main loop
    print("\nWelcome to the credit hour calculator!")
    fullName = input("What is your full name?: ")
    studentID = input("What is your student ID?: ")
    gradYear = input("What year will you graduate?: ")

    while True:
        print(f"\nHello {fullName}, your student ID is {studentID} and you will graduate in {gradYear}.")
        creditHourCalculate()

    
        resetCondition = input("\nWould you like to calculate again? (yes or no): ").strip().lower()
        if resetCondition == "no":
            break  # Exit inner loop and ask if they want to exit the program

    exitCondition = input("\nWould you like to exit the program? (yes or no): ").strip().lower()
    if exitCondition == "yes":
        print("\nThank you for using the Credit Hour Calculator! Goodbye!")
    break