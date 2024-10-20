class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n + 1)
        steps[0] = 1
        for i in range(1, n + 1):
            steps[i] += steps[i - 1]
            if i - 2 >= 0:
                steps[i] += steps[i - 2]
        return steps[n]