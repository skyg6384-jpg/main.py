# if __name__ == "__main__": (this script can be imported or run standalone)
#Functions and classes in this module can be reused without the main block of code executing.
#Good practice (code is modular,
#               helps improve readability.
#               leaves no global variables.
#               avoids unintended execution)

#               Ex: library = import library for functionality
#                   When running the library directly, display a help page


def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is Script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()