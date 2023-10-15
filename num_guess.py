print("Enter the integer for the play to guess.")
player_guess = int(input())
tries = 0

while True:
    if tries == 0:
        guess = int(input("Enter your guess.\n"))
    else:
        guess = int(input())

tries += 1
if guess > player_guess:
    print("Too high - try again:")
elif guess < player_guess:
    print("Too low - try again")
elif guess == player_guess:
    print("You guessed it in", tries, "tries.")
    