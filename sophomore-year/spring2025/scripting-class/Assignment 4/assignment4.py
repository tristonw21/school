#assignment4 - 

"""
Re use the code from the previous assignment but modify it to fit these new instructions. We want the entire program to loop on repeat until the user stops it so dont get rid of that.
We want the user to be able to select one of the options to enter hours into instead of asking for all 4, one at a time.
Modify the program to display an at the moment of number of hours entered by the user. 
"""



def creditHourCalculator():
    creditHours = 0  # total credit hours
    while True:
        print("\nWhat would you like to do?")
        print("1. Add 1-credit hour classes")
        print("2. Add 2-credit hour classes")
        print("3. Add 3-credit hour classes")
        print("4. Add 4-credit hour classes")
        print("5. Finish and calculate total")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 5:
                break  # Exit this loop to return total hours
            elif choice < 1 or choice > 5:
                print("Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        # Ask how many classes of the chosen type
        try:
            num_classes = int(input("How many classes?: "))
            if num_classes < 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        # Add to credit hour total based on the type
        if choice == 1:
            creditHours += 1 * num_classes
        elif choice == 2:
            creditHours += 2 * num_classes
        elif choice == 3:
            creditHours += 3 * num_classes
        elif choice == 4:
            creditHours += 4 * num_classes

        print(f"\nCurrent total credit hours: {creditHours}")

    return creditHours

while True: #Main Loop
    print("\nWelcome to the Credit Hour Calculator!")
    fullName = input("What is your full name?: ")
    studentID = input("What is your student ID?: ")
    gradYear = input("What is your graduation year?: ")

    while True:
        print (f"\nHello {fullName}, your student ID is {studentID} and you are graduating in {gradYear}.")
        totalHours = creditHourCalculator()  # Call the function to calculate credit hours

        # Evaluate total hours
        if totalHours > 12:
            print(f"\nYou are taking {totalHours} credit hours this semester. You're doing great! Keep it up!")
        elif totalHours < 9:
            print(f"\nYou are taking {totalHours} credit hours this semester. You could do better than that!")
        else:
            print(f"\nYou are taking {totalHours} credit hours this semester. You're doing okay.")

        resetCondition = input("\nWould you like to calculate again? (yes/no): ").strip().lower()
        if resetCondition == "no":
            print("Thanks for using the Credit Hour Calculator, Goodbye!")
            break
        elif resetCondition != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue