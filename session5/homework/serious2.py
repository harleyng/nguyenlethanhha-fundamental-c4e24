prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0

for fruit in prices:
    print(fruit)
    print("price:", prices[fruit])
    for fr in stock:
        if fruit == fr:
            print("stock:", stock[fr])
            print()

            sell = prices[fruit] * stock[fr]
            total += sell

print(total)


        
    
          