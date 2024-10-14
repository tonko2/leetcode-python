class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = []
        for c in s:
            if c.isalnum():
                alnum.append(c.lower())
        return alnum == alnum[::-1]