# Code taken from in-class example

def BubbleSort(myList): # Bubble Sort Algorithm
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = \
                           myList[j + 1], myList[j]
    return myList

