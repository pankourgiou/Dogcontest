# Needed to create random numbers to simulate dice roll
import random

# Initialise player scores to 0
player1_score = 0
player2_score = 0
player3_score = 0
player4_score = 0
# Repeat everything in this block 10 times
for i in range(10):

    # Generate random numbers between 1 and 6 for each player.
    player1_value = random.randint(1, 100)
    player2_value = random.randint(1, 100)
    player3_value = random.randint(1, 100)
    player4_value = random.randint(1, 100)
    # Display the values
    print("Player 1 rolled: ", player1_value)
    print("Player 2 rolled: ", player2_value)
    print("Player 3 rolled: ", player3_value)
    print("Player 4 rolled: ", player4_value)
    # Selection: based on comparison of the values, take the appropriate path through the code.
    if player1_value > player2_value:
        print("player 1 wins-->You can choose to buy a Boxer")
        player1_score = player1_score + 1  # This is how we increment a variable
    elif player2_value > player1_value:
        print("player 2 wins-->You can choose to buy a German shepherd")
        player2_score = player2_score + 1
    else:
        print("It's a draw-->you can adopt a dog")
    if player1_value > player3_value:
        print("player 1 wins-->You can choose to buy a Boxer")
        player1_score = player3_score + 1  # This is how we increment a variable
    elif player2_value > player3_value:
        print("player 2 wins-->You can choose to buy a German shepherd")
        player2_score = player3_score + 1
    else:
        print("It's a draw-->you can adopt a dog")
    if player2_value > player3_value:
        print("player 2 wins-->You can choose to buy a Boxer")
        player2_score = player3_score + 1  # This is how we increment a variable
    elif player2_value > player3_value:
        print("player 2 wins-->You can choose to buy a German shepherd")
        player2_score = player2_score + 1
    else:
        print("It's a draw-->you can adopt a dog")
    if player4_value > player3_value:
        print("player 4 wins-->You can choose to buy a Boxer")
        player4_score = player3_score + 1  # This is how we increment a variable
    elif player4_value > player3_value:
        print("player 4 wins-->You can choose to buy a German shepherd")
        player2_score = player2_score + 1
    else:
        print("It's a draw-->you can adopt a dog")
    input("Press enter to continue.")  # Wait for user input to proceed.

print("### Game Over ###")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)
print("Player 3 score:", player3_score)
print("Player 4 score:", player4_score)
