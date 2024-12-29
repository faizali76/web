# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'hiscore.txt' which is either blank or contains the previous hi-score.You need to write a program to update the hi-score whenever game() breaks the hi-score.
import random # Random number generate karne ke liye

 # Step 1: Game ka score generate karo
def game():
     print("You are playing the game...")
     score = random.randint(1, 62)  # Random score 1 se 100 ke beech     # Fetch the hiscore 
     with open("hiscore.txt") as f:
         hiscore = f.read()
         if(hiscore!=""):
             hiscore = int(hiscore)
         else:
             hiscore = 0    
     print(f"Your score:{score}")
     if(score>hiscore ):
         #  Write this hiscore to the file
         with open("hiscore.txt", "w") as f:
             f.write(str(score))
     return score 
game()



# import random

# def game():
#     print("You are playing the game...")
#     score = random.randint(1, 65)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"Your score: {score}")
#     if(score>hiscore):
#         with open("hiscore.txt", "w") as f:
#            hiscore = f.read()
#            f.write(hiscore)

#     return score




# game()