import random

options = ("rock", "paper", "scissor")
player = None
player_score = 0
computer_score = 0
is_running = True

while is_running:
    computer = random.choice(options)
    while not player in options:
        player = input("Input your choice (rock, paper, scissor): ").lower()
    
    print(f"{player} vs {computer}", end=": ")
    if player == computer:
        print("TIE!")
    elif player == "rock" and computer == "scissor":
        print("YOU WIN!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("YOU WIN!")
        player_score += 1
    elif player == "scissor" and computer == "paper":
        print("YOU WIN!")
        player_score += 1
    else:
        print("YOU LOSE!")
        computer_score += 1

    print(f"""-----
You : Computer
{player_score} : {computer_score}
-----""")

    if not input("Play again?(y/n): ") == "y":
        is_running = False
    player = None

print(f"""-----
Your final score is:
You : Computer
{player_score} : {computer_score}""")
print("Thanks for playing!")