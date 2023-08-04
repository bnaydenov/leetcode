class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # https://youtu.be/-moq8WgNRsY
        # O(n + m)

        if len(ransomNote) > len(magazine):
            return False

        dict = {}

        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for char in ransomNote:
            if char not in dict:
                return False
            else:
                if dict[char] == 0:
                    return False
            dict[char] -= 1

        return True
