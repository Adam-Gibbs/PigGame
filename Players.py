import random

class Player:

    def __init__(self, name):
        self.score = 0
        self.stats = {'Pigs': 0, 'Wins': 0, 'Losses': 0}
        self.multiplyer = 1

    def roll(self):

        total = 0
        pigs = 0

        for die in range(3):
            result = random.randint(1, 6)

            if result == 2:
                pigs += 1
                self.stats['Pigs'] += 1
            
            else:
                total += result

        return ((total * self.multiplyer), pigs)


