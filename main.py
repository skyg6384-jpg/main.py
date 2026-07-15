# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                  inner loop:

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()

# project rectangle using nested loop.

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()