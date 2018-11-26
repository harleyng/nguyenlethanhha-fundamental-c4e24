a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
c = int(input("Enter number c:"))

delta = b*b - 4*a*c
a2 = a*2

if delta < 0:
    print("There is no solution")
elif delta == 0:
    print("1 Solution")
    x = (-b) / a2
    print(x)
else:
    print("2 Solutions")
    delta_sqrt = delta**0.5
    x1 = (-b + delta_sqrt) / a2
    x2 = (-b - delta_sqrt) / a2
    print("x1 = " x1)
    print("x2 = " x2)



