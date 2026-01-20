#Random number generator using the python random module
import random

limit = int(input("How many chance do you want to guess?: "))
high = int(input("What's the max number threshold do you want to guess?: "))

number = random.randint(1, high)
for i in range(limit):
    
    print(f"{limit} guesses left!")
    guess = int(input("Insert your guesses: "))
    if guess == number:
        print("You're correct!")
        break
    elif guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
    else:
        print("Invalid!")
    
    limit -= 1

if guess != number:
    print("You LOSE!")
else:
    print(f"Congrats! You succeeded after {i} tries!")