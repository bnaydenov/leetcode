class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # https://youtu.be/Gjkhm1gYIMw

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
