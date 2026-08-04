# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} year old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("Sky God", 21)
happy_birthday("Tyson", 42)
happy_birthday("Tom", 28)


# Example

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ₹{amount:.2f} is due: {due_date}")

display_invoice("Sky God", 6000, "01/08/2026")
display_invoice("Tyson", 500000, "05/08/2026")
display_invoice("tom", 100500.32, "05/09/2028")

# -----------------
# -----------------

# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


# Example

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Sky", "God")

print(full_name)