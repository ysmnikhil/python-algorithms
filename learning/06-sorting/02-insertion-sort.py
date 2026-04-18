'''
Insertion sort: Find the right position for each element
Array will be sort by piece by piece, we will select the value and compare it with the left value and continue to do that and replace the min value until we reach the starting of array for each loop.
time complexity | O(n2) | as we two loops
time complexity best case | O(n) | we will never go to inner loop
space complexity | O(1) 

Think of insertion sort like organizing a hand of playing cards. When you pick up cards one by one, you don't search through your entire hand to find the smallest card to place first (that would be selection sort). Instead, you take each new card and slide it into its proper position among the cards you're already holding in order. This natural, intuitive process is exactly how insertion sort works.
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
# print(sort([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
