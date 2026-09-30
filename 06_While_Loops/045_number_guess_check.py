guess = 7

while True:
    user_guess = int(input("Guess the number (between 1 and 10): "))
    if user_guess < guess:
        print("Too low! Try again.")
    elif user_guess > guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
    