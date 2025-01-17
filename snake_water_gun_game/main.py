# The rules for the Snake Water Gun game are as follows: 
# Snake vs. Water: The snake wins by drinking the water
# Water vs. Gun: The gun drowns in water, giving a point to water
# Gun vs. Snake: The gun kills the snake and wins
# Draw: If both players choose the same object, the result is a draw

import random
computer = random.choice([-1,0,1])
mapped_values = {"S":1, "W":-1, "G" : 0}
values_dict = {1:"Snake", 0:"Gun", -1:"Water"}
player2_input = input("Press S for Snake and G for Gun and W for Water: ")
player2_value = mapped_values[player2_input] #s:1

print(f"You chose {values_dict[player2_value]} and computer chose {values_dict[computer]}")
if (computer==player2_value):
    print("Its a draw!!!")
else:
    if((computer == 1) and (player2_value == -1)):      # Snake vs Water
        print("Computer Wins!!!")
    elif((computer == 1) and (player2_value == 0)):     # Snake vs Gun
        print("You win!!!")
    elif((computer == -1) and (player2_value == 1)):    # Water vs Snake
        print("You win!!!")
    elif((computer == -1) and (player2_value == 0)):    # Water vs Gun
        print("Computer win!!!")
    elif((computer == 0) and (player2_value == 1)):     # Gun vs Snake
        print("Computer win!!!")
    elif((computer == 0) and (player2_value == -1)):    # Gun vs Water
        print("You win!!!")
    else:
        print("Something went wrong!!!")
    


