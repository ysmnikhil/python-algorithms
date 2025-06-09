'''
Heap:
O(nlogn)
but as we compare the results from top to bottom the work becomes less and the complexity will become O(n)
'''

def heap_up(ll, idx) :
    while idx > 0:
        parentIdx = (idx - 1)//2
        if ll[parentIdx] < ll[idx]:
            prt = ll[parentIdx]
            ll[parentIdx] = ll[idx]
            ll[idx] = prt
            idx = parentIdx
        else:
            break

    return ll

def heap_insert(ll, value) :
    return heap_up(ll, value)

def heap_down(ll, idx, heap_size) :
    while idx < heap_size:
        largestIdx = idx
        left_child = idx*2 + 1
        right_child = idx*2 + 2
        if left_child < heap_size and ll[left_child] > ll[largestIdx]:
            largestIdx = left_child

        if right_child < heap_size and ll[right_child] > ll[largestIdx]:
            largestIdx = right_child
        
        if idx != largestIdx:
            prt = ll[largestIdx]
            ll[largestIdx] = ll[idx]
            ll[idx] = prt
            idx = largestIdx
        else:
            break

    return ll

def heapify (listOfValues):
    lenOfValues = len(listOfValues) - 1 
    
    for i in range(lenOfValues//2, -1, -1):
        listOfValues = heap_down(listOfValues, i, lenOfValues)

    return listOfValues

def heapify_up (listOfValues):
    lenOfValues = len(listOfValues)
    
    for i in range(lenOfValues):
        ll = heap_up(listOfValues, i)

    return ll

def extract_max(ll) :
    # swap with last element
    ll[0] = ll[len(ll) - 1]
    del ll[len(ll) - 1]
    ll = heap_down(ll, 0, len(ll))
    return ll 

def max_sorted_values (ll):
    v = []
    i = 0
    while len(ll) > 0:
        v.append(ll[0])
        ll = extract_max(ll)
    return v

print(heapify([2, 6, 1, 7, 9, 9, 4]))
print(max_sorted_values(heapify([2, 6, 1, 7, 9, 9, 4])))
print(heapify_up([2, 6, 1, 7, 9, 9, 4]))
print(max_sorted_values(heapify_up([2, 6, 1, 7, 9, 9, 4])))

print(heapify([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
print(max_sorted_values(heapify([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7])))
print(heapify_up([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
print(max_sorted_values(heapify_up([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7])))
