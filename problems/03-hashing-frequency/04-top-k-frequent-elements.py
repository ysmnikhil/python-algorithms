'''
Phase 2 — Hashing & Counting
🧠 Problem: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You can return the answer in any order.

Example
    nums = [1,1,1,2,2,3]
    k = 2
    # Output: [1,2]

    nums = [1]
    k = 1
    # Output: [1]

Important constraints
    You should aim for better than sorting the whole array
    Ideal: O(n) time

The pattern menu 🍽️
There are 2 standard correct approaches:

- ✅ Approach A: Bucket Sort (O(n))
    Count frequencies using dict
    Create buckets: bucket[freq] = list of numbers
    Iterate buckets from high freq → low, collect until k
    This is the “I know DSA patterns” solution.

- ✅ Approach B: Heap (O(n log k))
    Count frequencies
    Maintain min-heap of size k
    This is simpler sometimes, but bucket is cleaner and faster.
'''

def top_k_frequent(arr_frq, k):
    freq = {}
    n = len(arr_frq)
    buckets = [[] for _ in range(n + 1)]
    for i in arr_frq:
        freq[i] = freq.get(i, 0) + 1

    for f in freq.keys():
        buckets[freq[f]].append(f)

    res = []
    # kk = k
    for val in range(n, 0, -1):
        # res += buckets[val][:kk]
        # kk -= len(buckets[val])
        # if kk <= 0:
        #     break

        for num in buckets[val]:
            res.append(num)
            if len(res) == k:
                return res
        
    return res

if __name__ == "__main__":
    print(top_k_frequent([11,1,4,5,1,3,5,4,9,1,2,3,3, 4], 4))