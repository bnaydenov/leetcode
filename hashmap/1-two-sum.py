class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # https://anontube.lvkaszus.pl/watch?v=KLlXCFG5TnA

        prevMap = {}  # val, index

        for i, n in enumerate(nums):
            diff = target - i
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
