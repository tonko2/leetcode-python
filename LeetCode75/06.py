class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(s.strip().split()[::-1]))