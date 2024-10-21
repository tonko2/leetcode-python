        
class Solution:
    def compress(self, chars: List[str]) -> int:
        def getNumAsStr(x):
            res = []
            while x:
                res.append(str(x % 10))
                x //= 10
            return res[::-1]
        pos = 0
        prev_char = ""
        ans_cnt = 0
        while pos < len(chars):
            cnt = 0
            if prev_char != chars[pos]:
                prev_char = chars[pos]
                cnt = 1
                pos += 1
            while pos < len(chars) and prev_char == chars[pos]:
                pos += 1
                cnt += 1
            chars[ans_cnt] = prev_char
            ans_cnt += 1
            if cnt > 1:                
                for c in getNumAsStr(cnt):
                    chars[ans_cnt] = c
                    ans_cnt += 1
        chars = chars[:ans_cnt]
        return len(chars)