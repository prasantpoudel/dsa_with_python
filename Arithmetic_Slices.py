"""
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[defaultdict(int), defaultdict(int)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][0][d] += 1
                dp[i][1][d] += dp[j][0][d] + dp[j][1][d]
        return sum(map(lambda x: sum(x[1].values()), dp))
