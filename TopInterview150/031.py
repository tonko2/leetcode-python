from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        alphabet = defaultdict(int)
        for i in range(len(s)):
            if alphabet[s[i]] == 0:
                alphabet[s[i]] += 1
            else:
                while left < i and alphabet[s[i]]:
                    alphabet[s[left]] -= 1
                    left += 1
                alphabet[s[i]] += 1
            ans = max(ans, i - left + 1)
        return ans