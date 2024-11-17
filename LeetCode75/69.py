class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bit = format(a, f'0{32}b')
        b_bit = format(b, f'0{32}b')
        c_bit = format(c, f'0{32}b')
        ans = 0
        for i in range(len(c_bit)):
            if c_bit[i] == '0':
                if a_bit[i] == '1':
                    ans += 1
                if b_bit[i] == '1':
                    ans += 1
            elif c_bit[i] == '1' and a_bit[i] == '0' and b_bit[i] == '0':
                ans += 1
        return ans