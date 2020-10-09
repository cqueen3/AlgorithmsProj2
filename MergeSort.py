#from https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort
#with minor modifications
#taken from in-class example

def MergeSort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = MergeSort(left)
    right = MergeSort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

a = [1, 5634, 34, 3, 6, 4, 6745, 234 ,34, 6,2 ,456]
print(MergeSort(a))