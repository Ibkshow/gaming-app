import random
# scoreboard count step1
head_count = 0
tail_count =0

# game loop step 2
while True:
    print("tossing the coin...")
    toss = random.choice(["heads", "tails"])

    # step 3 update the count
    if toss == "heads":
        head_count +=1
    else:
        tail_count +=1

        # step 4 results and scoreboard
    print("results:",toss)
    print(f"scoreboard -heads:{head_count}, tails:{tail_count}")

    # step 5 ask the user if they want to play again or not
    play_again = input("toss again? (yes/no): ")
    if play_again.lower() != "yes":
        print("goodbye!")
        break