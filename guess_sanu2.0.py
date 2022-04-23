import random

value = random.randint(0, 10)  # the number which we have to guess
g = 0
chance = 5

print("GUESS THE NUMBER 1 - 10")
while True:
    guess = int(input('Enter Your Number: '))
    g = g + 1
    if g == chance + 1:
        print("YOU LOSE")
        input2 = int(input("For Start/Continue press: 1\nFor Exit/Stop press: 0 "))
        if input2 == 1:
            continue
        elif input2 == 0:
            break
        else:
            print("INVALID INPUT")
            break
    elif guess < value:
        print("Enter Grater Value")
    elif guess > value:
        print("Enter Smaller Value")
    else:
        print("YOU WIN", "Your Score Is", ((100 - (g * chance)) // g))
        print("You Use", g, "Out Of", chance, "Guesses")
        input2 = int(input("For Start/Continue press: 1\nFor Exit/Stop press: 0 "))
        if input2 == 1:
            continue
        elif input2 == 0:
            break
        else:
            print("INVALID INPUT")
            break
