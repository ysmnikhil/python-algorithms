def reverse_array(arr):
    a = arr.copy()

    left = 0
    right = len(a) - 1

    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

    return a

if __name__ == "__main__":
    print(reverArray([1, 2, 3, 4, 5, 6, 7, 8]))
