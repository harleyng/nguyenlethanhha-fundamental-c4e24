word = "courageous"
characters = list(word)

# decoration
print("Welcom to hangman")
print()
hangman = ["-", "-", "-", " ", " "]
print(*hangman)
for _ in range(5):
    print()

# print out the blank
blank = []
for _ in range(len(word)):
    blank.append("_ ")
print(*blank)

print()

# identify index for each character 

    
# user guess
guess_live = 8  
loop = True
while loop:
    user_guess = input("Your guess? ")

    for i in range(len(characters)):
        if user_guess in characters:
            if user_guess == characters[i]:
                blank[i] = user_guess           # replace user_guess in right index 
                print(*blank)   
                print()            # there is two valid results so it print two times
                if not "_ " in blank:
                    print("Congrats, you won")
                    loop = False 

           
    if not user_guess in characters: 
        guess_live -= 1 
        print(guess_live)
        if guess_live == 7:         
            print("---|")           

            print()
            print(*blank) 
            print()
            continue                  
        elif guess_live == 6:
            print("---|")
            print("   |")
            
            print()
            print(*blank)
            print() 
            continue
        elif guess_live == 5:
            print("---|")
            print("   |")
            print("   0")

            print()
            print(*blank) 
            print()
            continue
        elif guess_live == 4:
            print("---|")
            print("   |")
            print("   0")
            print("   |")

            print()
            print(*blank) 
            print()
            continue 
        elif guess_live == 3:
            print("---|")
            print("   |")
            print("   0")
            print("  -|")

            print()
            print(*blank)
            print() 
            continue 
        elif guess_live == 2:
            print("---|")
            print("   |")
            print("   0")
            print("  -|-")

            print()
            print(*blank) 
            print()
            continue
        elif guess_live == 1:
            print("---|")
            print("   |")
            print("   0")
            print("  -|-")
            print("  /")

            print()
            print(*blank) 
            print()
            continue
        elif guess_live == 0:
            print("---|")
            print("   |")
            print("   0")
            print("  -|-")
            print("  / \ ")

            print()
            print("You lost")
            loop = False 
                      # add element after each loop        # dung vong for cu moi mot lan ve xong dung break
    



