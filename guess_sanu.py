value = 5  # the number which we have to guess
g = 0
chance = 5
print("GUESS THE NUMBER 1 - 10\nenter your number ")
while True:
    guess = int(input())
    g = g + 1
    if g == chance + 1:
        print("YOU LOSE")
        break
    elif guess < value:
        print("enter grater value")
    elif guess > value:
        print("enter smaller value")
    else:
        print("YOU WIN")
        print("you use", guess, "out of", chance, "guesses")
        break
