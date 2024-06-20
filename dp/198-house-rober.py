class Solution:
    def rob(self, nums: List[int]) -> int:
        # https://youtu.be/VXqUQYGMnQg
        #
        # To solve this problem, we can use dynamic programming. We'll create an array max_amount where max_amount[i] represents the maximum amount of money we can rob from houses 0 to i.
        # For each house i, we have two options:
        # Rob the current house i, in which case we cannot rob the previous house i-1. So the total amount of money would be nums[i] + max_amount[i-2] (if i-2 exists).
        # Do not rob the current house i, in which case we can rob the previous house i-1. So the total amount of money would be max_amount[i-1].
        # We'll choose the option that gives us the maximum amount of money.
        # The time complexity of this solution is O(n) because we iterate through the nums array once.

        # if only 1 element return it
        if len(nums) < 2:
            return nums[0]

        dp = []

        dp.insert(0, nums[0])
        dp.insert(1, max(nums[0], nums[1]))

        for i in range(2, len(nums), 1):
            dp.insert(i, max(dp[i - 2] + nums[i], dp[i - 1]))

        return dp[-1]
