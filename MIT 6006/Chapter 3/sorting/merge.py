'''
Merge sort:
Array will be sort by dividing into sub-array and so on, we will select the value and compare it with the left value and continue to do that and replace the min value until we reach the starting of array for each loop.
'''

def divideForMerge (loV):
    lenOfLoV = len(loV)
    halfLenOfValue = lenOfLoV//2

    if lenOfLoV > 1:
        sortedf1 = divideForMerge(loV[:halfLenOfValue])
        sortedf2 = divideForMerge(loV[halfLenOfValue:])

        return mergeValues(sortedf1, sortedf2)

    return loV

def mergeValues (sortedf1, sortedf2):
    res = []

    i = j = 0

    while (i < len(sortedf1) and j < len(sortedf2)):
        if sortedf1[i] > sortedf2[j]:
            res.append(sortedf2[j])
            j += 1
        else:
            res.append(sortedf1[i])
            i += 1

    res = res + sortedf1[i:] + sortedf2[j:]

    return res

def sort (listOfValues):
    listOfValues = divideForMerge(listOfValues)

    return listOfValues

print(sort([2, 6, 1, 7, 9, 9, 4]))
print(sort([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
