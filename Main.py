import Players
import random
import time

def getPlayers():
    newPlayerName = input("Player Name: ")

    if newPlayerName != "":
        listplayers = getPlayers()
        listplayers.append(newPlayerName)
        return listplayers

    else:
        return list()

def makePlayers(playerList):
    return [Players.playerClass(playerList[count]) for count in range(len(playerList))]

def chooseOrder(playerList):
    
    orderList = list()
    while len(playerList) > 1:
        selection = random.choice(playerList)
        playerList.remove(selection)
        orderList.append(selection)

    orderList.append(playerList[0])
    return orderList

def isWin(playerList):
    if True in list(map(lambda x:x.checkWin(), playerList)):
        return True, playerList[(list(map(lambda x:x.checkWin(), playerList))).index(True)]
    
    else:
        return False, None

def playerTurn(currentPlayer):
    currentTotal = 0
    while input("\nPress [ENTER] to roll...\n") == "":
        roll, pigs = currentPlayer.roll()
        currentTotal += roll

        print("player ", currentPlayer.getName(), " rolled a total of ", roll, " and ", pigs, " pig[s]")

        if pigs == 1:
            break
        
        if pigs == 2:
            print("This your total is 0 and so their score is ", currentPlayer.getScore())
            return

        if pigs == 3:
            print("This resets your score to 1 :(")
            currentPlayer.resetScore()

        print("The total for the round of ", currentTotal)
    
    currentPlayer.addScore(currentTotal)
    print("Thus your round ends with a total score of ", currentPlayer.getScore())
    return
    
def resetPlayers(playerList):
    (list(map(lambda x:x.reset(), playerList)))

def setupGame():
    players = makePlayers(getPlayers())
    while len(players) < 2:
        print("\n\nYou need more than 1 player to play...")
        players = makePlayers(getPlayers())

    return(players)

def Main(players):
    while isWin(players)[0] == False:

        for player in players:
            time.sleep(2)
            print("\n\n\nPlayer ", player.getName(), "'s turn, current score of ", player.getScore())
            playerTurn(player)

    print("\n\n" + isWin(players)[1].getName() + " Has won!")
    resetPlayers(players)
    

createdPlayers = setupGame()
while input("\n\n\n\n\nPress [ENTER] to continue...\n") == "":
    Main(createdPlayers)
