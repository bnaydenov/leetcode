class Solution:
    def isHappy(self, n: int) -> bool:

        # https://youtu.be/ljz85bxOYJ0

        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSque(n)
            if n == 1:
                return True

        return False

    def sumOfSque(self, n: int) -> int:
        result = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            result += digit
            n = n // 10

        return result
