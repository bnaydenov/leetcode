class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # https://walkccc.me/LeetCode/problems/0026/
        # count = 0
        #
        # for i in range(len(nums)):
        #
        #     if (i < len(nums) - 1) and (nums[i] == nums[i + 1]):
        #         continue
        #     nums[count] = nums[i]
        #     count += 1
        #
        # return count

        # Time O(n) and Space O(n)
        # count = 0
        #
        # for num in nums:
        #     if count < 1 or num > nums[count - 1]:
        #         nums[count] = num
        #         count += 1
        # return count

        # https://youtu.be/DEJAZBq0FDA
