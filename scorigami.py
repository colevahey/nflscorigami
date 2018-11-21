import csv
from table import games_table

csv_file = open('saved.csv')
past_scores = csv.DictReader(csv_file)

class Location:
    def __init__(self, winnerPoints, loserPoints, gameNum):
        self.winnerPoints = winnerPoints
        self.loserPoints = loserPoints
        self.gameNum = gameNum
        self.numOccurred = 0

    def setNumber(self, num):
        self.numOccurred = num

    def checkPossible(self):
        if self.winnerPoints < self.loserPoints:
            return False
        elif self.loserPoints == 1 and (self.winnerPoints <= 7 and self.winnerPoints != 6):
            return False
        elif self.winnerPoints == 1 and self.loserPoints == 0:
            return False
        else:
            return True

    def setColor(self):
        if self.checkPossible():
            if self.numOccurred > 25:
                colNum = 22
            elif 12 < self.numOccurred <= 25:
                colNum = 28
            elif 5 < self.numOccurred <= 12:
                colNum = 34
            elif 3 < self.numOccurred <= 5:
                colNum = 40
            elif 1 < self.numOccurred <= 3:
                colNum = 46
            elif 0 < self.numOccurred <= 1:
                colNum = 82
            else:
                colNum = 230
        else:
            colNum = 232
        return f"\033[48;5;{colNum}m   \033[0m"


positions = []
# n is row number (loser score)
for n in range(76):
    # i is the game number
    for i in range(n*76,(n+1)*76):
        positions.append(Location((i-76*n),n, i))

for score in past_scores:
    for position in positions:
        if position.winnerPoints == int(score["PtsW"]) and position.loserPoints == int(score["PtsL"]):
            print(position.winnerPoints, position.loserPoints, sep="-")
            position.setNumber(int(score["Count"]))


positions = [position.setColor() for position in positions]

input("Press [ENTER] to continue")
print("\033[H\033[2J")
print(games_table.format(*positions))