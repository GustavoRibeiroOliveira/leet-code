class Solution:
    def compressedString(self, word: str) -> str:
        c = word[0]
        times = 0
        comp = ""
        for char in word:
            if char != c or times == 9:
                comp += str(times) + c
                c = char
                times = 1
            else:
                times += 1
        return comp + str(times) + c


teste = Solution()
print(teste.compressedString(word="aaaaaaaaaaaaaabb"))
