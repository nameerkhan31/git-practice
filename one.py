import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS =====")

while True:
    user = input("\nChoose rock, paper or scissors (or quit): ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Draw!")

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"\nYour Score: {user_score}")
    print(f"Computer Score: {computer_score}")

print("\n===== GAME OVER =====")
print(f"Final Score: {user_score} - {computer_score}")
print("Thanks for playing!")
