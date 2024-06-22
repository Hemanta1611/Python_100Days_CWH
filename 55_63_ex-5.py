import random 

# random.choice(list/dict/.., n) -- n: number of random sample
# to get random input in integer format: random.randint(0, 2)

dict = {"S": 0, "W": 1, "G": 2}
player_score = 0
computer_score = 0

n = int(input("How many number of times you want to play this game? : "))
print()
i = 0
while (i < n):
    playerinput = int(input("Player turn: (0 for snake, 1 for water & 2 for gun): "))
    computerinput = random.choice(list(dict.values()))
    print("Computer input:", computerinput)
    if(playerinput == computerinput):
        player_score = player_score + 0
        computer_score = computer_score + 0
    elif(playerinput == 0):
        if(computerinput == 1):
            player_score = player_score + 1
        else:
            computer_score = computer_score + 1
    elif(playerinput == 1):
        if(computerinput == 2):
            player_score = player_score + 1
        else:
            computer_score = computer_score + 1
    elif(playerinput == 2):
        if(computerinput == 0):
            player_score = player_score + 1
        else:
            computer_score = computer_score + 1
    else:
        print("Wrong Input By Player \t Give correct input i.e from 0, 1, or 2")
        i = i - 1
    i = i + 1


print("\n")
print("Player Score:", player_score)
print("Computer Score:", computer_score)

if (player_score == computer_score ):
    print("DRAW DRAW DRAW !!!")
elif( player_score > computer_score):
    print("WIN WIN WIN !!!")
else:
    print("LOSE LOSE LOSE !!!")





