'''
Phase 1 → Sliding Window Variable

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

def longest_substring(core_string):
    left = 0
    max_length = 0
    helper_sub_set = set()

    for right in range(len(core_string)):
        while core_string[right] in helper_sub_set:
            helper_sub_set.discard(core_string[left])
            left += 1

        helper_sub_set.add(core_string[right])

        max_length = max(max_length, len(helper_sub_set))

    return max_length

if __name__ == "__main__":
    print(longest_substring('abaccbaaaaa'))

'''
abccbaaaaa

abc
 bcc
  ccb
   cba
    baa
     aaa
      aaa
       aaa
'''