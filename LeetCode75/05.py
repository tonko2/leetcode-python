class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = ["a", "e", "i", "o", "u"]
        vowelPos = []
        for i, c in enumerate(s):
            if c.lower() in vowels:
                vowelPos.append((i, c))
        print(vowelPos)
        N = len(vowelPos)
        for i in range(N):
            index, c = vowelPos[i]
            index2, c2 = vowelPos[N - 1 - i]
            s_list[index2] = c
        return "".join(s_list)
