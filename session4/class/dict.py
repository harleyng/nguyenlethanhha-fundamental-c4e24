vegetable = {
    "A": "Apple",
    "B": "Banana"
}

print (*vegetable)

lookup = input("What do you wanna find? ")

if lookup in vegetable:
    print(vegetable[lookup])
else:
    print("No exist")