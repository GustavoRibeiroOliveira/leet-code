class Solution(object):
    def intToRoman(self, num):
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        i = 0
        string = ""

        while num > 0:
            if num >= numbers[i]:
                string += letters[i]
                num = num - numbers[i]
            else:
                i += 1
        return string


teste = Solution()
print(teste.intToRoman(3749))
