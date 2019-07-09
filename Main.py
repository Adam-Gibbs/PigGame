import Players
import random

def getPlayers():
    newplayer = input("Player Name: ")

    if newplayer != "":
        listplayers = getPlayers()
        listplayers.append(newplayer)
        return listplayers

    else:
        return list()

def chooseOrder(playerList):
    
    orderList = list()
    while len(playerList) > 1:
        selection = random.choice(playerList)
        playerList.remove(selection)
        orderList.append(selection)

    orderList.append(playerList[0])
    return orderList




def Main():
    players = getPlayers()
    while len(players) < 2:
        print("\n\nYou need more than 1 player to play...")
        players = getPlayers()

    players = chooseOrder(players)

Main()
