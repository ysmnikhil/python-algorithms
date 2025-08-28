'''
bubble sort
time complexity | O(n2) | as we two loops
time complexity best case | O(n) | we will go to inner loop once and then both will break
space complexity | O(1) 

Think of bubble sort like this: imagine you have a line of people that need to be arranged by height, but you can only compare and swap adjacent people. You'd walk down the line, and whenever you find two people standing next to each other in the wrong order, you'd ask them to swap places. After one complete pass through the line, the tallest person would have "bubbled up" to the end, even though you never directly moved them there - they got there through a series of adjacent swaps.
'''

def sorting(to_be_sorted):
    arr = to_be_sorted.copy()
    len_of_arr = len(arr) - 1
    for i in range(len_of_arr + 1):
        j = 0

        is_swapped = False
        while j < len_of_arr - i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
            j = j + 1
        
        if not is_swapped:
            break
        
    return arr

print("Sorting: ", sorting([2, 4, 4, 2, 5, 9, 11, 1, 7, 12, 13, 14, 15, 16]))
print("Sorting: ", sorting([10, 9, 7, 3]))
print("Sorting: ", sorting([1, 5, 6, 7, 2, 3, 4]))
print("Sorting: ", sorting([10, 1, 2, 3, 4, 9]))
print("Sorting: ", sorting([1, 1, 2, 3, 4, 9]))