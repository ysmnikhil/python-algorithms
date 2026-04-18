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

def ransome_note(ransome, magazine):
    if len(ransome) > len(magazine):
        return False

    mapper = {}
    for i in magazine:
        mapper[i] = mapper.get(i, 0) + 1

    for i in ransome:
        if mapper.get(i, 0) == 0:
            return False
        mapper[i] -= 1

    return True

if __name__ == "__main__":
    print(ransome_note('abb', 'aab'))