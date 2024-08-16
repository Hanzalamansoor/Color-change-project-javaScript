# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.


import random

def game():
    print("You are playing the game")
    score = random.randint(1, 62)
    
    # Fetch the highscore if it exists, else set hiscore to 0
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0  
    
    print(f"Your score: {score}")
    
    # score can never be less than hiscore because initialized hiscore is 0 so the new score will be saved in the hiscore
    if score > hiscore:
        # Write the new highscore to the file
        with open("hiscore.txt", "w") as f:  # Corrected 'hiscore.txt,w' to 'hiscore.txt', 'w'
            f.write(str(score))
    
    return score

# Play the game
game()
