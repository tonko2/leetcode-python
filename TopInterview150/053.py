class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = [p for p in path.split("/") if p.strip()]
        for s in path:
            if s == ".":
                pass
            elif s == "..":
                if stack:
                    stack.pop()                
            else:
                stack.append(s)   
            print(stack)
        return "/" + "/".join(stack)
    
if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/home/"))