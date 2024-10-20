class Solution:
    def reverseBits(self, n: int) -> int:
        reversedBit = bin(n)[2:][::-1]
        reversedBit += (32 - len(reversedBit)) * '0'
        return int(reversedBit, 2)