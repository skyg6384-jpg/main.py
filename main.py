# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

# -----------------------

# *args

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 5, 7, 11, 13, 17, 23, 31, 37, 41, 47, 51, 53, 57, 61, 67, 71, 73, 79, 83, 87, 91, 97))


# Example 2

def display_num(*args):
    for arg in args:
        print(arg, end=" ")
    print()
    print()

display_num("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# ------------

# **kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.",
              city="Fake City",
              state="Fake State",
              zip="Fake Zip",
              country="Fake Country")
print()


# ----------------
# Both *args & **kwargs together

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
      print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Fake City",
               state="Fake State",
               zip="Fake Zip",
               country="Fake Country")