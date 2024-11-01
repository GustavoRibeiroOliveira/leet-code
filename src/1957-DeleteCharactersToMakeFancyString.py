class Solution:
    def makeFancyString(self, s: str) -> str:
        last_char = ""
        last_last_char = ""
        new_string = ""
        if len(s) <= 2:
            return s

        index = 0
        for char in s:
            if index == 0:
                last_last_char = char
                new_string += char
            elif index == 1:
                last_char = char
                new_string += char
            else:
                if char == last_char == last_last_char:
                    pass
                else:
                    last_last_char = last_char
                    last_char = char
                    new_string += char
            index += 1
        return new_string


teste = Solution()
print(teste.makeFancyString(s="leeetcode"))
