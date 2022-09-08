class Solution:
    # O(n) time | O(n) space
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        start = 0
        max_freq = 0
        count = defaultdict(int)

        for end in range(n):
            count[s[end]] += 1
            max_freq = max(max_freq, count[s[end]])

            while (end - start + 1) - max_freq > k:
                count[s[start]] -= 1
                start += 1

            res = max(res, end - start + 1)

        return res