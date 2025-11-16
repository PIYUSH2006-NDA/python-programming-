import random
import time

CHOICES = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

VALID = {"r": "rock", "p": "paper", "s": "scissors",
         "rock": "rock", "paper": "paper", "scissors": "scissors"}

def get_player_choice():
    prompt = "Choose [R]ock, [P]aper, [S]cissors or [Q]uit: "
    while True:
        choice = input(prompt).strip().lower()
        if not choice:
            continue
        if choice in ("q", "quit"):
            return "quit"
        if choice in VALID:
            return VALID[choice]
        print("Invalid input. Try again.")

def decide_winner(player, comp):
    if player == comp:
        return "tie"
    wins = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    return "player" if (player, comp) in wins else "computer"

def show_round(player, comp):
    print(f"\nYou chose: {player.upper()}")
    print(CHOICES[player])
    print(f"Computer chose: {comp.upper()}")
    print(CHOICES[comp])

def play_match(best_of=5):
    target = best_of // 2 + 1
    score = {"player": 0, "computer": 0, "tie": 0}
    round_no = 1

    print(f"\n--- Best of {best_of} (first to {target}) ---")
    while score["player"] < target and score["computer"] < target:
        print(f"\nRound {round_no} — Score | You: {score['player']}  CPU: {score['computer']}  Ties: {score['tie']}")
        player = get_player_choice()
        if player == "quit":
            print("\nYou quit the match.")
            return None
        comp = random.choice(list(CHOICES.keys()))
        time.sleep(0.25)
        show_round(player, comp)
        result = decide_winner(player, comp)
        if result == "player":
            score["player"] += 1
            print("You win this round!")
        elif result == "computer":
            score["computer"] += 1
            print("Computer wins this round.")
        else:
            score["tie"] += 1
            print("It's a tie.")
        round_no += 1

    if score["player"] > score["computer"]:
        print(f"\nYou won the match! Final Score — You: {score['player']}  CPU: {score['computer']}")
    else:
        print(f"\nComputer won the match. Final Score — You: {score['player']}  CPU: {score['computer']}")
    return score

def main():
    print("Welcome to Rock–Paper–Scissors — Best of 5")
    print("Type r/p/s or full words. Type q to quit.\n")
    overall = {"matches_played": 0, "matches_won": 0, "matches_lost": 0, "matches_tied": 0}

    while True:
        print("\nMain Menu:")
        print("1) Play Best of 5")
        print("2) Play custom Best of N")
        print("3) Show overall stats")
        print("4) Quit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            result = play_match(5)
            if result is None:
                continue
        elif choice == "2":
            n = input("Enter odd number (3,5,7...): ").strip()
            if not n.isdigit() or int(n) % 2 == 0:
                print("Invalid number.")
                continue
            result = play_match(int(n))
            if result is None:
                continue
        elif choice == "3":
            print("\n=== Overall Stats ===")
            print(f"Matches played: {overall['matches_played']}")
            print(f"Matches won: {overall['matches_won']}")
            print(f"Matches lost: {overall['matches_lost']}")
            print(f"Matches tied: {overall['matches_tied']}")
            continue
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        overall["matches_played"] += 1
        if result["player"] > result["computer"]:
            overall["matches_won"] += 1
        elif result["player"] < result["computer"]:
            overall["matches_lost"] += 1
        else:
            overall["matches_tied"] += 1

if __name__ == "__main__":
    main()
