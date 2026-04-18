'''
Phase 1 — PREFIX SUM
Big Idea (one sentence)
    Instead of recomputing sums again and again,
    we store cumulative history so any range becomes O(1).

That’s the whole pattern.
----------

Why Prefix Sum Exists
Imagine:
    nums = [2, 4, 1, 3, 6]

You’re asked:
    What is the sum from index 1 → 3 ?

    Brute force:
    4 + 1 + 3 = O(n)

    Prefix sum idea:
    Build:
        P[i] = sum of nums[0..i]
        P = [2, 6, 7, 10, 16]

    Then:
        sum(l..r) = P[r] - P[l-1]

👉 O(1). No loop.

Core Pattern 🔒
    Prefix Array Definition
        P[0] = nums[0]
        P[i] = P[i-1] + nums[i]

    Range Query
        sum(l..r) = P[r] - P[l-1]

That identity powers an entire family of problems.

First Problem (Classic Gateway)
🧠 Subarray Sum Equals K

Given an array nums and integer k,
return the number of continuous subarrays whose sum equals k.

Example
    nums = [1,1,1], k = 2
    Output: 2
    Explanation: [1,1] at (0,1) and (1,2)

Why sliding window fails
    Because numbers can be:
        negative
        positive
        unordered

Window sum doesn’t behave monotonically → two pointers break.

Prefix sum + hashmap saves us.

Key Insight
If:
    prefix[r] - prefix[l-1] = k
then:
    prefix[l-1] = prefix[r] - k

So we just need to know:
    “Have we seen prefix sum = current_sum - k before?”

BOOM — hashmap time.
'''

def subarray_sum(nums, k):
    matches = 0
    curr = 0
    prefix_value = {0:1}
    
    for i in nums:
        curr += i
        
        find_key = curr - k
        
        if find_key in prefix_value:
            matches += prefix_value[find_key]
            
        prefix_value[curr] = prefix_value.get(curr, 0) + 1

    return matches

if __name__ == "__main__":
    print(subarray_sum([1,1,1], 2))      # 2
    print(subarray_sum([1,2,3], 3))      # 2
    print(subarray_sum([1,-1,0], 0))     # 3
    print(subarray_sum([3,4,7,2,-3,1,4,2], 7)) # 4