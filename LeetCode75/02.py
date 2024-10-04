import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        gcd = math.gcd(n, m)
        gcd_str = str2[:gcd]
        if gcd_str * (n // gcd) == str1 and gcd_str * (m // gcd) == str2:
            return gcd_str
        else:
            return ""