class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * n
        graph = []
        reversedGraph = []
        for i in range(n):
            graph.append([])
            reversedGraph.append([])
        for p, q in connections:
            graph[p].append(q)
            reversedGraph[q].append(p)
        cnt = 0
        def dfs(city):
            nonlocal cnt
            visited[city] = True
            for next in graph[city]:
                if visited[next] == False:
                    dfs(next)
            for next in reversedGraph[city]:
                if visited[next] == False:
                    cnt += 1
                    dfs(next)
                
        dfs(0)                
        return n - cnt - 1