import random

def randomLists():
    forwardsList1 = []
    backwardsList1 = []
    randList1 = []

    for x in range(100000):
        forwardsList1.append(x)
        backwardsList1.append(100000-x)
        randList1.append(random.randint(1, 50000))

    return forwardsList1,backwardsList1,randList1
    