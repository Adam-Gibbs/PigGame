from secrets import randbelow

class playerClass:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.stats = {'Pigs': 0, 'Wins': 0, 'Losses': 0}
        self.multiplyer = 1

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def getMultiplyer(self):
        return self.multiplyer

    def checkWin(self):
        if (self.score - 1) % 100 == 0:
            self.stats['Wins'] += 1
            self.stats['Losses'] -= 1
            self.multiplyer = 0.8
            return True
        
        else:
            return False

    def roll(self):

        total = 0
        pigs = 0

        for die in range(3):
            result = randbelow(6)
            result += 1

            if result == 2:
                pigs += 1
                self.stats['Pigs'] += 1
            
            else:
                total += result

        return (round(total * self.multiplyer), pigs)

    def addScore(self, value):
        self.score += value

    def resetScore(self):
        self.score = 0

    def reset(self):
        self.stats['Losses'] += 1
        self.score = 0
        self.multiplyer += 0.2


