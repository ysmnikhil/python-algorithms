'''
Phase 2 — Hashing & Counting
🧠 Problem 2: Ransom Note

You’re given two strings:
- ransomNote
- magazine

Return True if you can construct ransomNote using letters from magazine.

Rules (important):
- Each letter in magazine can be used at most once
- Order does not matter

Examples
    ransomNote = "a"
    magazine   = "b"
    → False

    ransomNote = "aa"
    magazine   = "aab"
    → True

Why this problem exists (read this carefully)
- This problem teaches a one-sided frequency constraint.
- In anagrams → counts must match exactly
- In ransom note → counts must be sufficient

That distinction is huge.

'''

def find_anagrams(s: str, p: str) -> list[int]:
    k = len(p)
    if k > len(s):
        return []

    def char_ord(ch) -> int:
        return ord(ch) - ord('a')

    need = [0] * 26
    window = [0] * 26
    matches = []

    for ch in p:
        need[char_ord(ch)] += 1

    for right in range(len(s)):
        window[char_ord(s[right])] += 1

        if right >= k:
            window[char_ord(s[right - k])] -= 1

        if right >= (k - 1) and window == need:
            matches.append(right - (k - 1))

    return matches

if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))  # [0, 6]
    print(find_anagrams("abab", "ab"))         # [0, 1, 2]
    print(find_anagrams("aaaaa", "aa"))        # [0, 1, 2, 3]
    print(find_anagrams("xyz", "a"))           # []