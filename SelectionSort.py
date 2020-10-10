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


