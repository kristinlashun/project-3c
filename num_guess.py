player_guess = int(input("Enter the integer for the player to guess."))
tries = 0

while True:
  guess = int(input("Enter your guess: "))
  tries += 1
  
  if guess > player_guess:
    print("Too high - try again:")
  elif guess < player_guess:
    print("Too low - try again:")
  elif guess == player_guess:
    print("You guessed it in", tries, "tries.")
    break