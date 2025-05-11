import random
import time

HEAD = "Head"
TAIL = "Tail"

def coin_toss():
    # Simulate flipping animation
    print("Flipping the coin...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    toss = random.randint(0, 1)
    return HEAD if toss == 0 else TAIL

# Initialize counters
total_flips = 0
head_count = 0
tail_count = 0

while True:
    play_again = input("\nDo you want to play?\n yes or no: ").strip().lower()

    if play_again == "no":
        print("\nThanks for playing!")
        print(f"Total Tosses: {total_flips}")
        print(f"Heads: {head_count}")
        print(f"Tails: {tail_count}")
        break

    elif play_again == "yes":
        result = coin_toss()
        total_flips += 1
        if result == HEAD:
            head_count += 1
        else:
            tail_count += 1
        print("The side that landed is: ", result)

    else:
        print("Invalid input!! Enter yes or no.")
