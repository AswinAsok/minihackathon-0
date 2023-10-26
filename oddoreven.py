import random

playerOneName = input("Enter the Name of Player One: ")


def coinToss():
    # Generate a random number (0 or 1)
    result = random.randint(0, 1)

    # Return "Heads" for 0 and "Tails" for 1
    if result == 0:
        return "Heads"
    else:
        return "Tails"
    

def userBatting(PlayerOne, PlayerTwo):
    userOut = False
    while (not userOut):
        computerChoice = random.randint(1, 6)
        PlayerTwo[3] += 1
        userRun = input("Ethra Run Edukkun(1,6): ")

        if (userRun == computerChoice):
            if (PlayerOne[2] == 0):
                print("You are Duck!")
            else:
                print("You are Out Dudee!!")

            print(PlayerTwo[0] + " needs " + PlayerOne[2]+1 + "Runs to win!")
            userOut = True
            break
        else:
            print(PlayerOne[0] + " Scored " + userRun + " Runs ")
            PlayerOne[2] += int(userRun)

        if(PlayerOne[2] > PlayerTwo[2] and PlayerTwo[3] == 24):
            print("You have won the match")

        PlayerTwo[3] += 1

        if (PlayerTwo[3] == 24):
            print("Number of Balls Exccedded")
            print(PlayerOne[0] + " has Scored " +
                  str(PlayerOne[2]) + " Runs in 24 balls")
            userOut = True

            if(PlayerOne[3] >= 24 and PlayerOne[2] < PlayerTwo[2]):
                print("Match has been Won by Player Two")


def computerBatting(PlayerOne, PlayerTwo):
    computerOut = False
    while (not computerOut):
        computerChoice = random.randint(1, 6)
        PlayerOne[3] += 1
        userRun = input("Ethra Run Edukkun[B](1,6): ")

        if (userRun == computerChoice):
            if (PlayerTwo[2] == 0):
                print("You are Duck!")
            else:
                print("You are Out Dudee!!")

            print(PlayerOne[0] + " needs " + PlayerTwo[2]+1 + " Runs to win!")
            computerOut = True
            break
        else:
            print(PlayerTwo[0] + " Scored " + computerChoice + " Runs ")
            PlayerTwo[2] += int(computerChoice)

        PlayerOne[3] += 1

        if(PlayerTwo[2] > PlayerOne[2] and PlayerOne[3] == 24):
            print("The match has been won by computer")

        if (PlayerOne[3] == 24):
            print("Number of Balls Exccedded")
            print(PlayerOne[0] + " has Scored " +
                  str(PlayerOne[2]) + " Runs in 24 balls ")
            computerOut = True

            if(PlayerTwo[3] >= 24 and PlayerTwo[2] < PlayerOne[2]):
                print("Match has been Won by Player Two")

        


def oddOrEven():
    PlayerOne = [playerOneName, "", 0, 0]
    PlayerTwo = ["Computer", "", 0, 0]

    # [username, playtype, runsScored, numberOfBalls]

    # Randomly choose between 0 and 1
    toss = random.randint(0, 1)
    currentPlayer = ""
    choice = ""

    if toss == 0:
        currentPlayer = PlayerOne[0]
    else:
        currentPlayer = PlayerTwo[0]

    print(currentPlayer + " has Won the Toss")

    if currentPlayer == "Computer":
        rand = random.randint(0, 1)
        choice = "Batting" if rand == 0 else "Bowling"
        print("Computer has choosen " + choice)
    else:
        choice = input(currentPlayer + " Enter your choice(Batting/Bowling): ")
        print(currentPlayer + " has choosen " + choice)

    if currentPlayer == PlayerOne[0]:
        PlayerOne[1] = choice
        if PlayerOne[1] == "Batting":
            PlayerTwo[1] = "Bowling"
        else:
            PlayerTwo[2] = "Batting"
    else:
        PlayerTwo[1] = choice
        if PlayerTwo[1] == "Batting":
            PlayerOne[1] = "Bowling"
        else:
            PlayerOne[1] = "Batting"

    if (PlayerOne[1] == "Batting"):
        userBatting(PlayerOne, PlayerTwo)
        computerBatting(PlayerOne, PlayerTwo)

    elif (PlayerTwo[1] == "Batting"):
        computerBatting(PlayerOne, PlayerTwo)
        userBatting(PlayerOne, PlayerTwo)


oddOrEven()


