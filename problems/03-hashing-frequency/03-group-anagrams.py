'''
Phase 2 — Hashing & Counting
🧠 Problem 1: Group Anagrams

This is where:
- Counting becomes a hash key
- You stop solving one case… and start organizing many efficiently

Problem
Given a list of strings strs, group the anagrams together.
Return a list of groups (order doesn’t matter).

Example
    strs = ["eat","tea","tan","ate","nat","bat"]
    # Output:
    # [["eat","tea","ate"],["tan","nat"],["bat"]]

Why this problem matters
This teaches a major Phase-2 skill:
    turn a string into a canonical representation
    so anagrams map to the same key

Rules
    ❌ No sorting allowed for the main solution (sorting is too easy)
    ✅ Use counting frequency as key (26 letters)
    ✅ Use hashmap key -> list of strings
'''

def group_anagrams(strs: list[str]) -> list[list[str]]:
    hashmaper = {}

    def idx(ss):
        return ord(ss) - ord('a')

    def get_hash(ss):
        need = [0] * 26
        for s in ss:
            need[idx(s)] += 1

        return tuple(need)

    for ss in strs:
        str_hash = get_hash(ss)
        # hashmaper[str_hash] = hashmaper.get(str_hash, []) + [ss]
        hashmaper.setdefault(str_hash, []).append(word)

    return list(hashmaper.values())

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))