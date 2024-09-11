import time

test_list = [2, 1, 5, 10, 1, 13, 7]

def bubbleSort (values):
    vs = values.copy()
    l = len(vs)
    swapped = True
    for i in range(l - 1):
        if not swapped:
            break
        for j in range(l - i - 1):
            if vs[j] > vs[j + 1]:
                vs[j], vs[j + 1] = vs[j + 1], vs[j]
                swapped = False

    return vs

def bubbleSortWhile(values):
    print()
    vs = values.copy()
    n = len(vs)
    while n > 1:
        new_n = 0
        for i in range(1, n):
            if vs[i - 1] > vs[i]:
                vs[i - 1], vs[i] = vs[i], vs[i - 1]
                new_n = i
        n = new_n
    
    return vs

# Example usage

start_time = time.time()
sorted_list = bubbleSort(test_list)
end_time = time.time()
print(f"Sorted list (bubbleSort): {sorted_list}")
print(f"Execution time: {end_time - start_time:.6f} seconds")


start_time = time.time()
sorted_list = bubbleSortWhile(test_list)
end_time = time.time()
print(f"Sorted list (bubbleSortWhile): {sorted_list}")
print(f"Execution time: {end_time - start_time:.6f} seconds")