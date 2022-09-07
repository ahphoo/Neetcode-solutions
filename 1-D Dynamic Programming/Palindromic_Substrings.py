class Solution:
    # O(n^2) time | O(1) space
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            count += self.countPalindromes(s, i, i)
            count += self.countPalindromes(s, i, i + 1)

        return count

    def countPalindromes(self, s, i, j):
        count = 0
        n = len(s)
        lo, hi = i, j

        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
            count += 1

        return count