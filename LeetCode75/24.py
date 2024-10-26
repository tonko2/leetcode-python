class Solution:
    def removeStars(self, s: str) -> str:
        N = len(s)
        cnt = 0
        ans = []
        for c in s[::-1]:
            if c == '*':
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                    continue
                else:
                    ans.append(c)
        return "".join(ans[::-1])
    