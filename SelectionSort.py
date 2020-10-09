# taken from educative.io/edpresso/how-to-implement-selection-sort-in-python
# minor changess
def SelectionSort(array):
  n = len(array)
  for i in range(n):
    minimum = i

    for j in range(i+1, n):
      if (array[j] < array[minimum]):
        minimum = j
    
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp
    
  return array


a = [1, 5634, 34, 3, 6, 4, 6745, 234 ,34, 6,2 ,456]
print(SelectionSort(a))