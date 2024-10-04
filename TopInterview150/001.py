class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = 0
        m = 0
        N = len(word1)
        M = len(word2)
        while n < N or m < M:
            if n < N:
                ans += word1[n]
                n += 1
            if m < M:
                ans += word2[m]
                m += 1
        return ans