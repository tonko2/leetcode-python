class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:        
        if n > 45 or k > n:
            return []
        res = []
        def dfs(index, currList, total):            
            if len(currList) == k: 
                if total == n:
                    res.append(currList)
                return
            for i in range(index, 10):
                currTotal = total + i
                if currTotal <= n:
                    dfs(i + 1 , currList + [i], currTotal)
                if currTotal > n:
                    return
        dfs(1,[],0)
        return res
        