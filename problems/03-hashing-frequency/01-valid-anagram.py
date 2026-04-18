'''
Phase 2 — Hashing & Counting
🧠 Problem 1: Valid Anagram

We start clean. Foundational. Sneakily important.

Given two strings s and t, return True if t is an anagram of s, otherwise False.

Rules
- Same characters
- Same counts
- Order does not matter

Examples
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False

Why this problem exists (pay attention)
- This problem teaches the core idea of Phase 2:
- Presence is not enough.
- Frequency matters.

A set will lie to you here.
'''

def is_anagram(str_compare, str_with):
    if len(str_compare) != len(str_with):
        return False

    mapper = {}
    for i in range(len(str_compare)):
        mapper[str_compare[i]] = mapper.get(str_compare[i], 0) + 1
        mapper[str_with[i]] = mapper.get(str_with[i], 0) - 1

    for val in mapper.values():
        if val != 0:
            return False

    return True

if __name__ == "__main__":
    print(is_anagram('anagram', 'nagaram'))