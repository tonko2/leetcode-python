class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(x: int):
            cnt = 0
            while x:
                if x % 2:
                    cnt += 1
                x //= 2
            return cnt
        ans = []
        for i in range(n + 1):
            ans.append(countBit(i))
        return ans