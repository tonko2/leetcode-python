class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        answers = dict()
        exists = dict()
        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            answers[(a, b)] = values[i]
            answers[(b, a)] = 1 / values[i]
            exists[a] = b
            exists[b] = a
        print(answers)
        for i in range(len(equations)):
            for j in range(len(equations)):
                a, b = equations[i][0], equations[i][1]
                c, d = equations[j][0], equations[j][1]
                if a not in exists or b not in exists or c not in exists or d not in exists:
                    continue
                print(f'a = {a}, b = {b}, c = {c}, d = {d}')
                if a == c:
                    answers[(b, d)] = answers[(b, a)] * answers[(c, d)]
                    answers[(d, b)] = 1 / answers[(b, d)]
                if a == d:
                    answers[(b, c)] = answers[(b, a)] * answers[(d, c)]
                    answers[(c, b)] = 1 / answers[(b, c)]
                if b == c:
                    answers[(a, d)] = answers[(a, b)] * answers[(c, d)]
                    answers[(d, a)] = 1 / answers[(a, d)]
                if b == d:
                    answers[(a, c)] = answers[(a, b)] * (1 / answers[(c, d)])
                    answers[(c, a)] = 1 / answers[(a, c)]
        ans = []
        for a, b in queries:
            if (a, b) in answers:
               ans.append(answers[(a,b)])
            else:
                ans.append(-1.0)
        return ans