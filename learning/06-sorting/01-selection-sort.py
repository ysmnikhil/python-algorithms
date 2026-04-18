'''
Selection sort: Find the right element for each position
Array will be sort by piece by piece, we will select the value and compare it with the right value and continue to do that and replace that until we reach the end of array for each loop.
time complexity | O(n2) | as we two loops
space complexity | O(1) 

Think of your algorithm as a methodical librarian who has a very specific routine. This librarian always examines every book in the unsorted section to find the smallest one, regardless of whether those books happen to already be in perfect order or complete chaos. The librarian's process never changes because the algorithm has no way to "peek ahead" and realize that less work might be needed.
'''
def sort (listOfValues):

    lenOfValues = len(listOfValues)
    for i in range(lenOfValues):
        indexOfLowValue = i

        # start the loop from i and till the length of loop
        '''
        for j in range(lenOfValues):
            if listOfValues[indexOfLowValue] > listOfValues[j] and indexOfLowValue < j:
                indexOfLowValue = j
        '''
        
        j = i + 1 
        while j < lenOfValues:
            if listOfValues[indexOfLowValue] > listOfValues[j]:
                indexOfLowValue = j
            j = j + 1

        v = listOfValues[i]
        listOfValues[i] = listOfValues[indexOfLowValue]
        listOfValues[indexOfLowValue] = v

    return listOfValues

# this logic is with early termination
# time complexity | O(n2) | as we two loops
# space complexity | O(1) 
def sorting(to_be_sorted):
    arr = to_be_sorted

    count = 0

    selection_memory = 0

    # length of array | n
    while count < len(arr) - 1:
        if selection_memory == len(arr) - 1:
            break

        # remaning length of array | n - k (count)
        swap_key = count
        for i in range(count, len(arr)):
            if arr[swap_key] > arr[i]:
                swap_key = i
        
        if swap_key != count:
            swap_element = arr[count]
            arr[count] = arr[swap_key]
            arr[swap_key] = swap_element

        count = count + 1

        for i in range(len(arr) - 1, count - 1, -1):
            if arr[i] > arr[i - 1]:
                if selection_memory < i:
                    selection_memory = i
            else:
                selection_memory = i - 1
        
    return arr

print("Sorting: ", sorting([2, 4, 4, 2, 5, 9, 11, 1, 7, 12, 13, 14, 15, 16]))
print("Sorting: ", sorting([10, 9, 7, 3]))
print("Sorting: ", sorting([1, 5, 6, 7, 2, 3, 4]))
print("Sorting: ", sorting([10, 1, 2, 3, 4, 9]))


print(sort([2, 6, 1, 7, 9, 9, 4]))
print(sort([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
