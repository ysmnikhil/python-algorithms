'''
Phase 2 — Hashing & Counting
🧠 Problem: Minimum Window Substring

Given two strings:
    s (source)
    t (target)

    Return the smallest substring of s that contains all characters of t (including duplicates).
    If no such substring exists, return "".

Example
    s = "ADOBECODEBANC"
    t = "ABC"
    Output = "BANC"

    s = "a"
    t = "aa"
    Output = ""

Why this problem is hard (truth)

This problem combines everything you’ve learned:
    variable sliding window
    frequency maps
    “valid vs invalid” window
    shrinking while valid
    tracking best answer
Most people:
    expand correctly ❌
    but don’t know when/how to shrink
    or lose the invariant

The ONE invariant (tattoo this mentally 🔒)
    The window is valid iff it contains all characters of t
    with required frequencies.

Everything you do exists to:
    reach validity
    maintain validity
    minimize length while valid

High-level strategy (NO CODE)
You will maintain:
    need → frequency map of t
    window → frequency map of current window in s
    formed → how many unique chars currently satisfy required count
    required → number of unique chars in t

Window behavior (this is key)
1️⃣ Expand right
    Add s[right] to window
    If a char count hits exactly what’s needed → formed += 1

2️⃣ When window becomes valid (formed == required)
    Try to shrink from left
    Update answer if smaller
    Shrink until invalid again

3️⃣ Continue expanding
    That’s it. That’s the engine.
'''
def min_window(s: str, t: str) -> str:
    if not s or not t or len(t) > len(s):
        return ""

    from collections import Counter

    need = Counter(t)
    window = {}

    required = len(need)
    formed = 0

    left = 0
    ans_len = float("inf")
    ans_left = 0

    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1

        if s[right] in need and window[s[right]] == need[s[right]]:
            formed += 1

        while formed == required:
            window_len = right - left + 1

            if window_len < ans_len:
                ans_len = window_len
                ans_left = left
            
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1

    return "" if ans_len == float("inf") else s[ans_left : ans_left + ans_len]

if __name__ == "__main__":
    print(min_window('ADOBECOAFEBANC', 'ABFAD')) # BANC