class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=P6RZZMu_maU

        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if this start of sequance a.k.a does not have left nighbor
            if (n - 1) not in numSet:
                lenght = 0
                while (n + lenght) in numSet:
                    lenght += 1
                longest = max(longest, lenght)
        return longest
