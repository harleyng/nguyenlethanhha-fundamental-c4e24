shop = ["T-Shirt", "Sweater"]

while True:
    items = input("Welcome to our shop, what do you want (C, R, U, D, E)? ").upper()

    if items == "C":
        new_item = input("Which item do you want to add? ")
        new_item = shop.append(new_item)
        print("Our items: ",end =" ")
        print(*shop,sep=", ")

    elif items == "R":
        print("Our items: ",end =" ")
        print(*shop,sep=", ")

    elif items == "U":
        position = int(input("What position do you want to update? "))
        if position - 1 > len(shop):
            print("Index out of range")
        else:
            new_item = input("What item do you want to update? ")
            shop[position -1] = new_item
            print("Our items: ",end =" ")
            print(*shop,sep=", ")

    elif items == "D":
        position = int(input("What position do you want to delete? "))
        if position -1 > len(shop):
            print("Index out of range")
        else:
            shop.pop(position -1)
            print("Our items: ",end =" ")
            print(*shop,sep=", ")
    
    elif items == "E":
        break


