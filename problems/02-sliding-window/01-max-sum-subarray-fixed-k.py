'''
Phase 1 → Sliding Window

Sliding Window is not “two pointers with vibes”, It’s about maintaining a moving invariant. Most people fail because they don’t know what the window represents

🧠 Problem 1: Maximum Sum Subarray of Size K. This is the cleanest entry point. No tricks. No distractions.

Problem
    You’re given:
        An array of integers nums
        An integer k

        Return the maximum sum of any contiguous subarray of size k.

    Example
        nums = [2, 1, 5, 1, 3, 2]
        k = 3
        # Output: 9
        # Explanation: subarray [5, 1, 3]


    Another:
        nums = [2, 3, 4, 1, 5]
        k = 2
        # Output: 7  -> [3, 4]

'''

def max_sum_subarray(nums, k):
    if k > len(nums):
        return None

    max_sum = current_sum = sum(nums[:k])

    for right in range(k, len(nums)):
        current_sum = current_sum - nums[right-k] + nums[right]
        max_sum = max(current_sum, max_sum)

    return max_sum

if __name__ == "__main__":
    print(max_sum_subarray([2, 3, 4, 1, 5, 3], 3))
