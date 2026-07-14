# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1,11):   # range function
    print(x)

print("HAPPY NEW YEAR!")
print("HAPPY NEW YEAR!")

for y in reversed(range(1, 11)):  # reversed range function
    print(y)

for z in range(1, 11, 2):  # 2 is steps
    print(z)


# Example using credit card number

credit_card = "1234-5678-9012-3456"

for card_num in credit_card:
    print(card_num)

# Example, Print numbers from 1 to 20. When the number is 13, continue skips it.

for n in range(1, 21):
    if n == 13:
        continue
    else:
        print(n)

# Example, numbers from 1 to 20. When the number is 13, break it.

for m in range(1, 21):
    if m == 13:
        break
    else:
        print(m)