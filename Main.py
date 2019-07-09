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


def Main():
    players = makePlayers(getPlayers())
    while len(players) < 2:
        print("\n\nYou need more than 1 player to play...")
        players = makePlayers(getPlayers())

    players = chooseOrder(players)

Main()
