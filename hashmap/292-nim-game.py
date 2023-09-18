class Solution:
    def canWinNim(self, n: int) -> bool:

        # https://youtu.be/iaVL7Z7rUw0

        if n % 4 == 0:
            return False

        return True
