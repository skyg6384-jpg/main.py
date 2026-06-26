# Exercise 2 Shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many world you like?: "))
total = price * quantity

print(f"You bought {quantity} X {item}/s")
print(f"Your total is ₹{total}")