print("Hello, my name is Ha and here is my flock")
sheep_size = [5, 7, 300, 90, 24, 50, 75]

after_one_month = [x+50 for x in sheep_size]
for i in range(4):
    print("MONTH " + str(i + 1) )

    print("One month has passed, now here is my flock")
    print(after_one_month)

    biggest = max(after_one_month)
    print("My biggest sheep has size " + str(biggest) + " let's shear it")

    print("After shearing here is my flock")
    big_index = after_one_month.index(biggest)
    after_one_month[big_index] = 8
    print(after_one_month)
    print()

    after_one_month = [x+50 for x in after_one_month]

print("My flock has size in total:",sum(after_one_month))
print("I would get ", sum(after_one_month), " * 2$ = ", sum(after_one_month)* 2,"$", sep="")


    