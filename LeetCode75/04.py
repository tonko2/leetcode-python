class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        if N == 1:
            if flowerbed[0] == 0:
                n -= 1
            return n <= 0
        for i in range(N - 1):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == N - 2:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i + 1] = 0
                    n -= 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            print(flowerbed)
            if n <= 0:
                return True
        return n <= 0