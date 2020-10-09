# from educative.io/edpresso/how-to-implement-quicksort-in-python
def QuickSort(a):

    size = len(a)
    
    #Base case
    if size < 2:
        return a
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, size): #Partitioning loop
         if a[i] <= a[0]:
              current_position += 1
              temp = a[i]
              a[i] = a[current_position]
              a[current_position] = temp

    temp = a[0]
    a[0] = a[current_position] 
    a[current_position] = temp #Brings pivot to it's appropriate position
    
    left = QuickSort(a[0:current_position]) #Sorts the elements to the left of pivot
    right = QuickSort(a[current_position+1:size]) #sorts the elements to the right of pivot

    a = left + [a[current_position]] + right #Merging everything together
    
    return a


a = [1, 5634, 34, 3, 6, 4, 6745, 234 ,34, 6,2 ,456]
print(QuickSort(a))