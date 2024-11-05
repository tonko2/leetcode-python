class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []        
        def dfs(combination, cnt, index):
            if cnt == k:
                if sum(combination) == n:                    
                    ans.append(combination)                
                return
            if index == 10 or cnt > k:
                return
            for i in range(index, 10):
                dfs(combination + [i], cnt + 1, index + 1)
                dfs(combination, cnt, index + 1)
        dfs([], 0, 1)
        return ans