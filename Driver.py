from BubbleSort import *
from P2Tester import *
from MergeSort import *
from QuickSort import *
from SelectionSort import *
import time

def BubbleSortAverage(r):
    Time1 = 0
    Time2 = 0
    Time3 = 0
    for i in range(1):
        F1,B1,R1 = randomLists()
        start1 = time.time()
        #Best Case Already Sorted
        F = BubbleSort(F1)
        end1 = time.time()
        Time1 +=(end1-start1)
        start2 = time.time()
        #Worse Case Backwards
        B = BubbleSort(B1)
        end2 = time.time()
        Time2 +=(end2-start2)
        start3 = time.time()
        #Average Random numbers
        R = BubbleSort(R1)
        end3 = time.time()
        Time3 +=(end3-start3)
        
    FinalT1=Time1/r
    FinalT2=Time2/r
    FinalT3=Time3/r
    print("BubbleSort")
    print("Best Case Average Time:    ",FinalT1)
    print("Average Case Average Time: ", FinalT3)
    print("Worst Case Average Time:   ", FinalT2)


def MergeSortAverage(r):
    Time1 = 0
    Time2 = 0
    Time3 = 0
    for i in range(1):
        #order of list does not change run time 
        F1,B1,R1 = randomLists()
        start1 = time.time()
        F = MergeSort(F1)
        end1 = time.time()
        Time1 +=(end1-start1)
        start2 = time.time()
        B = MergeSort(B1)
        end2 = time.time()
        Time2 +=(end2-start2)
        start3 = time.time()
        R = MergeSort(R1)
        end3 = time.time()
        Time3 +=(end3-start3)
        
    FinalT1=Time1/r
    FinalT2=Time2/r
    FinalT3=Time3/r
    print()
    print("MergeSort")
    print("Order Does not effect time of MergeSort")
    print("BestCase Already Sorted Average Time:         ",FinalT1)
    print("AverageCase Random Number List Average Time:  ", FinalT3)
    print("WorstCase Backwards Sorted List Average Time: ", FinalT2)
       


def SelectionSortAverage(r):
    Time1 = 0
    Time2 = 0
    Time3 = 0
    for i in range(1):
        #order of list does not change run time 
        F1,B1,R1 = randomLists()
        start1 = time.time()
        F = SelectionSort(F1)
        end1 = time.time()
        Time1 +=(end1-start1)
        start2 = time.time()
        B = SelectionSort(B1)
        end2 = time.time()
        Time2 +=(end2-start2)
        start3 = time.time()
        R = SelectionSort(R1)
        end3 = time.time()
        Time3 +=(end3-start3)

        
    FinalT1=Time1/r
    FinalT2=Time2/r
    FinalT3=Time3/r
    print()
    print("SelectionSort")
    print("Order Does not effect time of SelectionSort")
    print("BestCase Already Sorted Average Time:         ",FinalT1)
    print("Average Case Random Number List Average Time: ", FinalT3)
    print("WorstCase Backwards Sorted List Average Time: ", FinalT2)


def QuickSortAverage(r):
    Time1 = 0
    Time3 = 0
    for i in range(1):
        F1,B1,R1 = randomLists()
        start1 = time.time()
        #Worst Case
        #F = QuickSort(F1)
        F = quickSortIterative(F1,0,4999)
        end1 = time.time()
        Time1 +=(end1-start1)
        start3 = time.time()
        #Best and average Case
        R = QuickSort(R1)
        end3 = time.time()
        Time3 +=(end3-start3)

        
    FinalT1=Time1/r
    FinalT3=Time3/r
    print()
    print("QuickSort")
    print("Unsorted is BestCase Average Time:     ",FinalT3)
    print("Unsorted is Average Case Average Time: ",FinalT3)
    print("WorstCase is Sorted Average Time:      ",FinalT1)
    



BubbleSortAverage(3)
MergeSortAverage(3)
SelectionSortAverage(3)
QuickSortAverage(3)
