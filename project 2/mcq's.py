Word = ["Tomato"]
guessed_correctly = False  # Variable to keep track of whether the guess is correct

while not guessed_correctly:
    print("Which one is a fruit and a vegtable : 1) Orange  2) Apple  3) Tomato")
    guess = input("Answer: ")
    
    if guess in Word:
        print("Correct! You guessed it right.")
        guessed_correctly = True  # Exit the loop if the guess is correct
    else:
        print("Try again.")
