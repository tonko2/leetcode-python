class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        minLength = 200
        for str in strs:
            minLength = min(minLength, len(str))
        for i in range(minLength):
            c = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != c:
                    return "".join(ans)
            ans.append(c)
        return "".join(ans)