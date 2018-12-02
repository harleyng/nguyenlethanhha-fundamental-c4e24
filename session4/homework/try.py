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
loop = True
while loop:
    user_guess = input("Your guess? ")

    for i in range(len(characters)):
        if user_guess in characters:
            if user_guess == characters[i]:
                blank[i] = user_guess           # replace user_guess in right index 
                print(*blank)               # there is two valid results so it print two times
                if not "_ " in blank:
                    print("Congrats, you won")
                    loop = False 

    guess_live = 8          
    if not user_guess in characters: 
        for _ in range(8):
            guess_live -= 1
            if guess_live == 7:         # error: it doesnt minus after each loop and can draw by using list
                hangman[3] = "|"  
                print(*hangman)
                break                      
            elif guess_live == 6:
                 hangman[0] = " "       
                hangman[1] = " "
                hangman[2] = " "
               hangman[3] = "|"
                print(*hangman) 
                break
            elif guess_live == 5:
                hangman[3] = "0"
                print(*hangman)
                break 
            elif guess_live == 4:
                hangman[4] = "-"
                hangman[3] = "|"
                print(*hangman)
                break 
           elif guess_live == 3:
                hangman[2] = "-"
                print(*hangman)
                break 
            elif guess_live == 2:
                hangman[4] = "-"
                print(*hangman)
                break 
            elif guess_live == 1:
                hangman[2] = "/"
                hangman[3] = " "
                print(*hangman)
                break 
            elif guess_live == 0:
                hangman[4] = "\ "
                print(*hangman)
                print("You lost")
                loop = False 
                      # add element after each loop        # dung vong for cu moi mot lan ve xong dung break
    



