from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        N = len(senate)
        for i in range(N):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(N)
                N += 1
            else:
                dire.append(N)
                N += 1
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"