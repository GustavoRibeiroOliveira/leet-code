class Solution(object):
    def romanToInt(self, s):
        roman_to_number = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum = 0
        i = len(s)-1
        while i >= 0:
            if roman_to_number[s[i]] > roman_to_number[s[i-1]] and i != 0:
                sum += roman_to_number[s[i]] - roman_to_number[s[i-1]]
                i -= 1
            else:
                sum += roman_to_number[s[i]]
            i -= 1
        return sum


teste = Solution()
print(teste.romanToInt("III"))