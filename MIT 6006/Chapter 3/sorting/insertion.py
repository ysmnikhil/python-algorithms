'''
Insertion sort:
Array will be sort by piece by piece, we will select the value and compare it with the left value and continue to do that and replace the min value until we reach the starting of array for each loop.
'''
def sort (listOfValues):

    lenOfValues = len(listOfValues)
    for i in range(lenOfValues):
        j = i

        while j > 0 and listOfValues[j] < listOfValues[j - 1]:
            v = listOfValues[j]
            listOfValues[j] = listOfValues[j - 1]
            listOfValues[j-1] = v
            j = j - 1

    return listOfValues

print(sort([2, 6, 1, 7, 9, 9, 4]))
print(sort([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
