'''
Phase 2 — Hashing & Counting
🧠 Problem 3: Permutation in String

You’re given two strings:
    s1
    s2

    Return True if any permutation of s1 is a substring of s2.

Examples
    s1 = "ab"
    s2 = "eidbaooo"
    → True   # "ba"

    s1 = "ab"
    s2 = "eidboaoo"
    → False

Why this problem matters (no fluff)

This problem forces you to:
- Use a fixed-size sliding window
- Maintain frequency counts
- Compare state, not strings
- Avoid recomputing counts every time

Key insight (read slowly)
A permutation of s1 exists in s2 iff there exists a window in s2 of length len(s1) whose character frequencies exactly match s1.

So this is:
- Sliding Window (fixed size)
- Valid Anagram
- merged cleanly

Core invariant 🔒
At every step, the window of size len(s1) in s2 must be checked for frequency equality with s1.
- We don’t compare strings.
- We compare counts.

❌ What NOT to do
- Sorting every window (O(n·k·log k) = nope)
- Clearing and rebuilding maps per window
- Nested loops
- Comparing substrings directly
'''

def permutation_in_string(s1, s2):
    if len(s1) > len(s2):
        return False

    window_size = len(s1)

    frq_map_s1 = {}
    frq_map_s2 = {}

    for s in s1:
        idx = ord(s) - ord('a')
        print(idx)
        frq_map_s1[s] = frq_map_s1.get(s, 0) + 1

    right = 0
    left = 0
    while right < len(s2):
        frq_map_s2[s2[right]] = frq_map_s2.get(s2[right], 0) + 1

        right += 1

        if right - left > window_size:
            frq_map_s2[s2[left]] = frq_map_s2.get(s2[left], 0) - 1
            left += 1

        if right - left + 1 == window_size:
            is_mapped = True
            for i in frq_map_s1.keys():
                if frq_map_s1[i] != frq_map_s2.get(i, 0):
                    is_mapped = False
                    break
            
            if is_mapped:
                return True

    return False

if __name__ == "__main__":
    print(permutation_in_string('aac', 'aabssssccss'))