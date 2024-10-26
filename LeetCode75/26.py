import re

class Solution:
    def decodeString(self, s: str) -> str:
        def replace_with_repeated(match):    
            number = int(match.group(1))
            letters = match.group(2)
            return letters * number        
        pattern = r'(\d+)\[([a-z]+)\]'
        while True:
            prev_s = s            
            s = re.sub(pattern, replace_with_repeated, s)
            if prev_s == s:
                break
        return s