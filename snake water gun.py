import random
print("SNAKE WATER GUN GAME\n")
print("Write :\n s for snake\nw for water \n g for gun")
l = ['s','w','g']
chance = 0
tchance = 10
your = 0
opponent = 0
while chance < tchance:
    human = input("Enter snake water or gun :\n")
    hum = human.lower()
    comp = random.choice(l)
    if comp == hum:
        print(f"You plays {hum} and opponent plays {comp}")
        print("It's a Tie.")
    elif hum =='w' and comp == 's':
        opponent = opponent + 1
        print(f"You plays {hum} and opponent plays {comp}")
        print("snake drinks water , You lost")
        print(f"opponent points are {opponent} , your points are {your}")
    elif hum == 'w' and comp == 'g':
        your = your + 1
        print(f"You plays {hum} and opponent plays {comp}")
        print("gun sinks in water , You won")
        print(f"opponent points are {opponent} , your points are {your}")
    elif hum == 's' and comp == 'g':
        opponent = opponent + 1
        print(f"You plays {hum} and opponent plays {comp}")
        print("gun kills snake , You lost")
        print(f"opponent points are {opponent} , your points are {your}")
    elif hum == 's' and comp == 'w':
        your = your + 1
        print(f"You plays {hum} and opponent plays {comp}")
        print("snake drinks water , You won")
        print(f"opponent points are {opponent} , your points are {your}")
    elif hum == 'g' and comp == 's':
        your = your + 1
        print(f"You plays {hum} and opponent plays {comp}")
        print("gun kills snake , You won")
        print(f"opponent points are {opponent} , your points are {your}")
    elif hum == 'g' and comp == 'w':
        opponent = opponent + 1
        print(f"You plays {hum} and opponent plays {comp}")
        print("gun sinks in water , You lost")
        print(f"opponent points are {opponent} , your points are {your}")
    else:
        print("wrong input")
    chance = chance + 1
    print(f"{tchance - chance} chance left out of {tchance}")
print("GAME OVER\n")
if your > opponent:
    print(f"your total points are {your} and opponents are {opponent}")
    print(f"you won by {your - opponent} points")
elif your == opponent:
    print(f"your total points are {your} and opponents are {opponent}")
    print("It's a tie.")
else:
    print(f"your total points are {your} and opponents are {opponent}")
    print(f"opponent won by {opponent - your} points")

