from BubbleSort import *
from P2Tester import *
import time

def BubbleSortAverage():
    Time1 = 0
    Time2 = 0
    Time3 = 0
    for i in range(30):
        F1,B1,R1 = randomLists()
        start1 = time.time()
        F = BubbleSort(F1)
        end1 = time.time()
        Time1 +=(end1-start1)
        start2 = time.time()
        B = BubbleSort(B1)
        end2 = time.time()
        Time2 +=(end2-start2)
        start3 = time.time()
        R = BubbleSort(R1)
        end3 = time.time()
        Time3 +=(end3-start3)
        
    FinalT1=Time1/30
    FinalT2=Time2/30
    FinalT3=Time3/30
    print(FinalT1)
    print(FinalT2)
    print(FinalT3)
       


BubbleSortAverage()
