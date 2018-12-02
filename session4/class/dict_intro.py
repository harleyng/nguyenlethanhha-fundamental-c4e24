# person = {}
# print(person)
# print(type(person))

person = {
    "name": "H.Duc",
    "city": "Hai Phong",
    "age": 25
}

print(person["name"])
# print("name" in person) #Boolean
if "name" in person:
    print("Yes")
else:
    print("No")