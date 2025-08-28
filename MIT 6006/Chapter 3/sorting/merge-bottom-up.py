# merge sort | bottom-up
# time complexity | O(nlong) | as we have 1 loop and then dividing the array in 2 parts which we become logn
# space complexity | O(1) 
def merge(left, right):
    arr = []
    
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            arr.append(right[j])
            j = j + 1
        else:
            arr.append(left[i])
            i = i + 1

    arr = arr + left[i:] + right[j:]

    return arr

def divide_and_merge(arr):
    if len(arr) <= 1:  # Handle edge case
        return arr
    
    n = len(arr)
    width = 1
    while width < n:
        print(f"width {width}")
        print(f"range {range(0, n, 2*width)}")
        for i in range(0, n, 2*width):
            print(f"i {i}")
            left = arr[i:i+width]
            right = arr[i+width:i+2*width]
            print(f"left {left}")
            print(f"right {right}")
            print(f"i:i+2*width {i, i+2*width}")

            arr[i:i+2*width] = merge(left, right)
        width *= 2
    return arr

def sort(to_be_sorted):
    arr = to_be_sorted.copy()
    return divide_and_merge(arr)

print(sort([2, 6, 1, 7, 9, 9, 4]))
print(sort([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))

