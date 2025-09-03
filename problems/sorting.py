# quick sort
# time complexity | O(nlogn) | worst case O(n2)
# space complexity | O(1) 
import random

def pivot_random (arr, start, end):
    pivot = arr[random.randint(start, end)]
    return pivot

def pivot_median (arr, start, end):
    mid = ( start + end ) // 2
    first = arr[start]
    middle = arr[mid]
    last = arr[end]

    if first >= middle >= last or last >= middle >= first:
        return middle
    elif middle >= first >= last or last >= first >= middle:
        return first
    else:
        return last

def partition(to_be_sorted, pivot):
    smaller = []
    equal = []
    larger = []
    print(to_be_sorted)
    print(pivot)
    for i in range(len(to_be_sorted)):
        if to_be_sorted[i] > pivot:
            larger.append(to_be_sorted[i])
        elif to_be_sorted[i] == pivot:
            equal.append(to_be_sorted[i])
        else:
            smaller.append(to_be_sorted[i])

    result = smaller + equal + larger
    return result, len(smaller) 

def sort (to_be_sorted):
    result = partition(to_be_sorted, pivot_median(to_be_sorted, 0, len(to_be_sorted) - 1))
    return result

print(sort([2, 6, 1, 7, 9, 9, 4]))
# print(sort([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))

