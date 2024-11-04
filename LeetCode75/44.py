class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [False] * N
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for i, connected in enumerate(isConnected[node]):
                if connected:
                    dfs(i)
        ans = 0
        for i in range(N):
            if visited[i] == False:
                dfs(i)
                ans += 1
        return ans