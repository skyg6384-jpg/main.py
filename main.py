# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")
hello("Hello", last="Mr.", title="John", first="Cena")
hello("Hello", title="Mr.", last="John", first="James")


# Example 1

for x in range(1, 11):
    print(x, end=" ")
print()

# Example 2

print("1", "2", "3", "4", "5", sep="-")


#Exercise

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=123, first=456, last=7890)
print(phone_num)