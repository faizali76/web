# import random
# '''
# 1 for sanke
# -1 for water
# 0 for gun
# '''
# computer = random.choice([-1, 0, 1])
# youstr = input("Enter your choice: ")
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDic = {1: "Snake", -1: "Water", 0: "Gun"}

# you = youDict[youstr]

# print(f"You chose {reverseDic[you]}\ncomputer chose{reverseDic[computer]}")

# if(computer == you):
#     print("Its a draw")

# else:
#     if(computer == -1 and you ==1):
#         print("You win")

#     elif(computer == -1 and you ==0):
#         print("You lose!")

#     elif(computer ==1 and you ==-1):
#         print("You lose!")

#     elif(computer ==1 and you ==0):
#         print("You win!")    

#     elif(computer ==0 and you ==-1):
#         print("You win!")

#     elif(computer ==0 and you ==1):
#         print("You lose!")

#     else:
#         print("something went wrong!")
import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

def play_game():
    # Randomly choose one for the computer (1 = Snake, -1 = Water, 0 = Gun)
    computer = random.choice([-1, 0, 1])

    # Ask user for their choice
    youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").strip().lower()

    # Mapping user input to the corresponding numbers
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDic = {1: "Snake", -1: "Water", 0: "Gun"}

    # Validate user input
    if youstr not in youDict:
        print("Invalid input! Please enter 's' for Snake, 'w' for Water, or 'g' for Gun.")
        return

    you = youDict[youstr]

    # Print the choices
    print(f"\nYou chose {reverseDic[you]}")
    print(f"Computer chose {reverseDic[computer]}")

    # Determine the result of the game
    if computer == you:
        print("It's a draw!")
    else:
        if computer == -1 and you == 1:
            print("You win! Snake drinks Water.")
        elif computer == -1 and you == 0:
            print("You lose! Water douses Gun.")
        elif computer == 1 and you == -1:
            print("You lose! Snake drinks Water.")
        elif computer == 1 and you == 0:
            print("You win! Gun shoots Snake.")
        elif computer == 0 and you == -1:
            print("You win! Water douses Gun.")
        elif computer == 0 and you == 1:
            print("You lose! Gun shoots Snake.")

# Run the game
def main():
    while True:
        play_game()
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    main()
