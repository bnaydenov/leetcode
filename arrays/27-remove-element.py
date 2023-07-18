class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time O(n) and Space O(1)
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count
