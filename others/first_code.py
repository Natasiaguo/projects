import random

play = input("rock, paper, or scissors? ")
random_ints = random.randint(1, 3)
if random_ints == 1:
    print("The computer's play: Rock")
elif random_ints == 2:
    print("The computer's play: paper")
else:
    print("The computer's play: scissors")
if random_ints == 1 and play == "rock":
    print("It's a tie!")
elif random_ints == 1 and play == "paper":
    print("You win!")
elif random_ints == 1 and play == "scissors":
    print("You lose!")
elif random_ints == 2 and play == "rock":
    print("You lose!")
elif random_ints == 2 and play == "paper":
    print("It's a tie!")
elif random_ints == 2 and play == "scissors":
    print("You win!")
elif random_ints == 3 and play == "rock":
    print("You win!")
elif random_ints == 3 and play == "paper":
    print("You lose!")
elif random_ints == 3 and play == "scissors":
    print("It's a tie!")