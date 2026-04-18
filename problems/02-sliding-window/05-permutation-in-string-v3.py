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

    for ch in s1:
        need[idx(ch)] += 1

    for i in range(k):
        window[idx(s2[i])] += 1

    # matches = how many positions i have window[i] == need[i]
    matches = 0
    for i in range(26):
        if window[i] == need[i]:
            matches += 1

    if matches == 26:
        return True

    # Slide
    for right in range(k, n):
        enter = idx(s2[right])
        exit_ = idx(s2[right - k])

        # Before updating enter: if it was matching, it will stop matching
        if window[enter] == need[enter]:
            matches -= 1
        window[enter] += 1
        if window[enter] == need[enter]:
            matches += 1

        # Before updating exit: if it was matching, it will stop matching
        if window[exit_] == need[exit_]:
            matches -= 1
        window[exit_] -= 1
        if window[exit_] == need[exit_]:
            matches += 1

        if matches == 26:
            return True

    return False

if __name__ == "__main__":
    print(permutation_in_string('ab', 'aabssssccss'))