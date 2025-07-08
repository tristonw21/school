def mad_lib_invasion():
    print("\n--- Invasion Mad Lib ---")
    noun = input("Enter a noun: ")
    city = input("Enter a city: ")
    number = input("Enter a number: ")
    period_of_time = input("Enter a period of time: ")
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    person_name = input("Enter a person's name: ")
    clothing = input("Enter a type of clothing: ")
    color = input("Enter a color: ")

    story = (f"\nIt is a little known fact that {noun}s have been watching {city} for {number} {period_of_time}. "
             f"Only the {adj1} people believed that it was just a matter of time before {noun}s invaded the {adj2} city of {city}. "
             f"{person_name}, who was a {adj1} person tried to warn the people, telling them their best defense was to hang "
             f"{clothing}s from the trees and {color} shoes on every door knob. Unfortunately no one believed {person_name} and "
             f"when {noun}s attacked {city}, only the {adj1} people survived.\n")
    print(story)


def mad_lib_romeo_and_juliet():
    print("\n--- Romeo and Juliet Mad Lib ---")
    noun_plural1 = input("Enter a plural noun: ")
    place = input("Enter a place: ")
    noun1 = input("Enter a noun: ")
    noun_plural2 = input("Enter another plural noun: ")
    noun2 = input("Enter another noun: ")
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    number = input("Enter a number: ")
    verb1 = input("Enter a verb: ")
    body_part = input("Enter a body part: ")
    verb2 = input("Enter another verb: ")

    story = (
        f"\nTwo {noun_plural1}, both alike in dignity,\n"
        f"In fair {place}, where we lay our scene,\n"
        f"From ancient {noun1} break to new mutiny,\n"
        f"Where civil blood makes civil hands unclean.\n"
        f"From forth the fatal loins of these two foes\n"
        f"A pair of star-cross`d {noun_plural2} take their life;\n"
        f"Whole misadventured piteous overthrows\n"
        f"Do with their {noun2} bury their parents` strife.\n"
        f"The fearful passage of their {adj1} love,\n"
        f"And the continuance of their parents` rage,\n"
        f"Which, but their children`s end, nought could {verb1},\n"
        f"Is now the {number} hours` traffic of our stage;\n"
        f"The which if you with {adj2} {body_part} attend,\n"
        f"What here shall {verb2}, our toil shall strive to mend.\n"
    )
    print(story)


def mad_lib_walmart():
    print("\n--- Walmart Mad Lib ---")
    verb1 = input("Enter a verb: ")
    adj1 = input("Enter an adjective: ")
    noun_plural1 = input("Enter a plural noun: ")
    adj2 = input("Enter another adjective: ")
    verb_ing = input("Enter a verb ending in 'ing': ")
    verb2 = input("Enter another verb: ")
    number = input("Enter a number: ")
    adj3 = input("Enter another adjective: ")
    noun_plural2 = input("Enter another plural noun: ")
    noun_plural3 = input("Enter another plural noun: ")
    noun_plural4 = input("Enter another plural noun: ")
    relative_plural = input("Enter a plural family member (e.g., 'cousins'): ")
    adj4 = input("Enter another adjective: ")
    adj5 = input("Enter another adjective: ")
    noun_plural5 = input("Enter another plural noun: ")

    story = (f"\nCome {verb1} at WALMART, where you'll receive {adj1} discounts on all of your favorite brand name {noun_plural1}. "
             f"Our {adj2} and {verb_ing} associates are there to {verb2} you {number} hours a day. "
             f"Here you will find {adj3} prices on the {noun_plural2} you need. "
             f"{noun_plural3} for the moms, {noun_plural4} for the kids and all the latest electronics for the {relative_plural}. "
             f"So come on down to your {adj4} {adj5} WALMART where the {noun_plural5} come first.\n")
    print(story)


while True:
    print("\n=== Mad Lib Generator ===")
    print("1. Invasion")
    print("2. Romeo and Juliet")
    print("3. Walmart")
    print("4. Exit")

    choice = input("Choose a Mad Lib (1-3) or 4 to Exit: ")

    if choice == "1":
        mad_lib_invasion()
    elif choice == "2":
        mad_lib_romeo_and_juliet()
    elif choice == "3":
        mad_lib_walmart()
    elif choice == "4":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        continue

    again = input("Would you like to go again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("\nBack to main menu...\n")
