import random

def randomLists():
    forwardsList1 = []
    backwardsList1 = []
    randList1 = []
   
    for x in range(5000):
        forwardsList1.append(x)
        backwardsList1.append(10000-x)
        randList1.append(random.randint(1, 50000))
   
    return forwardsList1,backwardsList1,randList1
    
    #forwardsList2 = []
    #backwardsList2 = []
    #randList2 = []
    #
    #
    #for x in range(10000):
    #    forwardsList2.append(x)
    #    backwardsList2.append(10000-x)
    #    randList2.append(random.randint(1, 50000))
    #return forwardsList2,backwardsList2,randList2

    #forwardsList3 = []
    #backwardsList3 = []
    #randList3 = []
    #
    #for x in range(100000):
    #    forwardsList3.append(x)
    #    backwardsList3.append(10000-x)
    #    randList3.append(random.randint(1, 50000))
    #return forwardsList3,backwardsList3,randList3