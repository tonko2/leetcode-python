class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s_list = []
        for c in s:
            if c in vowels:
                s_list.append('A')
            else:
                s_list.append(c)
        ans = 0
        s = "".join(s_list)
        for i in range(len(s) - k + 1):
            ans = max(ans, s[i:k].count("A"))
        return ans