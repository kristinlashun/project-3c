player_guess = int(input("Enter the integer for the player to guess.\n"))
tries = 0  

while True:  
    if tries == 0:
        print("Enter your guess.")  
    guess = int(input())  
    tries += 1  

    if guess > player_guess:
        print("Too high - try again:")
    elif guess < player_guess:
        print("Too low - try again:")
    elif guess == player_guess:
        if tries == 1:
            print("You guessed it in 1 try.")
        else:
            print("You guessed it in", tries, "tries.")
        break   