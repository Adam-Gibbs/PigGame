import Players
import random

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


def Main():
    players = makePlayers(getPlayers())
    while len(players) < 2:
        print("\n\nYou need more than 1 player to play...")
        players = makePlayers(getPlayers())

    while isWin(players)[0] == False:
        for player in players:
            player.roll()
            print(player.getName())

    print("\n\n" + isWin(players)[1].getName() + " Has won!")

            

Main()
