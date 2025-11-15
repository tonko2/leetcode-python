from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        genes = ['A', 'C', 'G', 'T']
        visited = set()
        q = deque()
        q.append((0, startGene))
        while q:
            mutate, gene = q.popleft()
            if gene == endGene:
                return mutate
            visited.add(gene)            
            for i in range(len(gene)):
                geneList = list(gene)
                for j in range(len(genes)):
                    geneList[i] = genes[j]
                    geneStr = "".join(geneList)
                    if geneStr in visited or geneStr not in bank:
                        continue
                    q.append((mutate + 1, geneStr))
        return -1
    
    
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
s = Solution()
print(s.minMutation(startGene, endGene, bank))

