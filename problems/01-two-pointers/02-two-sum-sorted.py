'''
Phase 1 — Two Pointers (Real Use Case)
🧠 Problem 3: Two Sum (Sorted Array)

You’re given:
- A sorted list of integers nums
- An integer target

Task:
Return the indices (0-based) of the two numbers such that:
    nums[i] + nums[j] == target

Constraints (read this carefully):
- The array is sorted in ascending order
- Exactly one solution exists
- You must not use extra space (no hash maps)
- Use two pointers

Example
    nums = [2, 7, 11, 15]
    target = 9
    # Output: [0, 1]

'''

def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1
        else :
            left += 1

    return None

if __name__ == "__main__":
    print(two_sum_sorted([1, 3, 4, 6, 10], 7))
