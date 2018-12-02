from random import randint

word_list = ["hexagon", "meticulous", "champion"]
#select randomly a word

i = randint(0, (len(word_list) - 1))
w = word_list[i]
word = word_list[i]
    
for _ in range(len(w)):                #print selected characters
    j = randint(0, (len(w) - 1))
    w = list(w)
    ch = w[j]
    print(ch,end=" ")
    w.pop(j)
print()

user_guess = input("Your answer: ")
if user_guess == word:
    print("True")
else:
    print(":(")

    

        

