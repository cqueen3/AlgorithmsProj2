import random

forwardsList = []
backwardsList = []
randList = []

for x in range(10000):
    forwardsList.append(x)
    backwardsList.append(10000-x)
    randList.append(random.randint(1, 50000))
    