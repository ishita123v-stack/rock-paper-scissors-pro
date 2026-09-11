import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    print("=" * 40)
    print("Welcome to Rock, Paper, Scissors Pro!")
    print("Type 'quit' at any time to exit the game.")
    print("=" * 40)

while True:
        # 1. Get user input and clean it up
        user_choice = input("\nEnter rock, paper, or scissors: ").lower().strip()

        if user_choice == "quit":
            break

        if user_choice not in choices:
            print("❌ Invalid choice! Please type 'rock', 'paper', or 'scissors'.")
            continue

        # 2. Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

# 3. Determine the winner of the round
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1

  # 4. Display current scoreboard
        print(f"📊 Score -> You: {user_score} | Computer: {computer_score}")

    # Final game over screen
    print("\n" + "=" * 40)
    print("🎮 GAME OVER 🎮")
    print(f"Final Standing -> You: {user_score} | Computer: {computer_score}")
    
    if user_score > computer_score:
        print("🏆 Congratulations! You beat the computer!")
    elif user_score < computer_score:
        print("🤖 The machines won this time. Better luck next time!")
    else:
        print("🤝 It ended in an absolute tie!")
    print("=" * 40)

if __name__ == "__main__":
    play_game()
