n = int(input("Enter a number: "))

for i in range(n//2):
    print("x", end=" ")
    print("*", end=" ")
if n % 2 == 1:
    print("x", end=" ")


print()
