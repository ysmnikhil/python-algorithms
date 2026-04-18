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

def permutation_in_string(s1: str, s2: str) -> bool:
    k = len(s1)
    n = len(s2)

    if k > n:
        return False

    def idx(ch: str) -> int:
        return ord(ch) - ord('a')

    need = [0] * 26
    window = [0] * 26

    # Build counts for s1 and first window in s2
    for ch in s1:
        need[idx(ch)] += 1

    for i in range(k):
        window[idx(s2[i])] += 1

    if window == need:
        return True

    # Slide the window
    for right in range(k, n):
        window[idx(s2[right])] += 1             # entering
        window[idx(s2[right - k])] -= 1         # exiting

        print(window)
        print(need)
        if window == need:
            return True

    return False

if __name__ == "__main__":
    print(permutation_in_string('ab', 'aabssssccss'))