'''
Selection sort:
Array will be sort by piece by piece, we will select the value and compare it with the right value and continue to do that and replace that until we reach the end of array for each loop.
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

print(sort([2, 6, 1, 7, 9, 9, 4]))
print(sort([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
