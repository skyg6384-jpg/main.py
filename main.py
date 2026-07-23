# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"India": "New Delhi",
            "USA": "Washington D.C.",
            "Russia": "Moscow",
            "China": "beijing"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("India"))
print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Pakistan"})
capitals.pop("China")
capitals.popitem()
#capitals.clear()

print(capitals)

keys = capitals.keys()

print(keys)

for key in capitals.keys():
    print(key)


values = capitals.values()
print(values)

for value in capitals.values():
    print(value)


items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
