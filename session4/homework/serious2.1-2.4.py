#2.1
print("Hello, my name is Ha and these are my sheep sizes ")
sheep_size = [5, 7, 300, 90, 24, 50, 75]
print(sheep_size)
print()

#2.2
biggest = max(sheep_size)
print("My biggest sheep has size " + str(biggest) + " let's shear it")
print()

#2.3
print("After shearing here is my flock")
big_index = sheep_size.index(biggest)
sheep_size[big_index] = 8
print(sheep_size)
print()


#2.4 
print("One month has passed, now here is my flock")
after_one_month = [x+50 for x in sheep_size]
print(after_one_month)
print()

