class Solution:
    # O(nlog(n)) time | O(n) space - Greedy solution with Binary Search
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # dp[i] represents the index of the last number in an LIS of length i.
        ans = 0  # The maximum length LIS in dp.

        # Try to place each num in an LIS.
        for i, num in enumerate(nums):
            idx = self.binarySearch(num, nums, ans, dp)  # Do binary search on the lengths of each LIS (which are sorted by default).
            dp[idx] = i
            ans = max(ans, idx)  # Update ans with the length of the longest LIS.

        return ans

    def binarySearch(self, num, nums, hi, dp):
        lo = 1

        while lo <= hi:
            mid = (lo + hi) // 2
            j = dp[mid]  # dp[mid] is the index of the last number in an LIS of length mid.

            if nums[j] >= num:  # If the last number is >= num, we know all LIS longer than it will also have the last number >= num.
                hi = mid - 1
            else:
                lo = mid + 1  # If the last number is < num, we know all LIS shorter than it will alo have last number < num.

        return lo