# format specifiers = {:flags} format a value based on what
#                              flags are inserted

price1 = 30000.6789
price2 = -50000.6789
price3 = 12000.34

# .(number)f = round to that many decimal places (fixed point)

print(f"Price 1 is ₹{price1:.2f}")
print(f"Price 2 is ₹{price2:.2f}")
print(f"Price 3 is ₹{price3:.2f}")

# :(number) = allocate that many spaces

print(f"Price 1 is ₹{price1:10}")
print(f"Price 2 is ₹{price2:10}")
print(f"Price 3 is ₹{price3:10}")

# :0(number) = allocate and zero pad that many spaces

print(f"Price 1 is ₹{price1:010}")
print(f"Price 2 is ₹{price2:010}")
print(f"Price 3 is ₹{price3:010}")

# :<(number) = left justify

print(f"Price 1 is ₹{price1:<10}")
print(f"Price 2 is ₹{price2:<10}")
print(f"Price 3 is ₹{price3:<10}")

# :>(number) = .right justify

print(f"Price 1 is ₹{price1:>10}")
print(f"Price 2 is ₹{price2:>10}")
print(f"Price 3 is ₹{price3:>10}")

# :^(number) = center align

print(f"Price 1 is ₹{price1:^10}")
print(f"Price 2 is ₹{price2:^10}")
print(f"Price 3 is ₹{price3:^10}")

# :+ = use a plus sign to indicate positive value

print(f"Price 1 is ₹{price1:+}")
print(f"Price 2 is ₹{price2:+}")
print(f"Price 3 is ₹{price3:+}")

# := = place sign to leftmost position

print(f"Price 1 is ₹{price1:=}")
print(f"Price 2 is ₹{price2:=}")
print(f"Price 3 is ₹{price3:=}")

# :  = insert a space before position numbers

print(f"Price 1 is ₹{price1: }")
print(f"Price 2 is ₹{price2: }")
print(f"Price 3 is ₹{price3: }")

# :, = comma separator

print(f"Price 1 is ₹{price1:,}")
print(f"Price 2 is ₹{price2:,}")
print(f"Price 3 is ₹{price3:,}")


# Exercise Mix Method

print(f"Price 1 is ₹{price1:+,.2f}")
print(f"Price 2 is ₹{price2:+,.2f}")
print(f"Price 3 is ₹{price3:+,.2f}")