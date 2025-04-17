from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for str in strs:
            d[''.join(sorted(str))].append(str)

        ans = []
        for key, value in d.items():
            ans.append(value)
        return ans