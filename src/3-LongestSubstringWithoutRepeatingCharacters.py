class Solution(object):
    def lengthOfLongestSubstring(self, s):
        repeatedCharacters = []
        maxLength = 0
        tempMaxLength = 0
        i = 0
        while i < len(s):
            if s[i] in repeatedCharacters:
                repeatedCharacters = []
                if tempMaxLength > maxLength:
                    maxLength = tempMaxLength
                i -= tempMaxLength
                tempMaxLength = 0
            else:
                tempMaxLength += 1
                repeatedCharacters.append(s[i])
            i += 1
        if tempMaxLength > maxLength:
            maxLength = tempMaxLength
        return maxLength


teste = Solution()
print(teste.lengthOfLongestSubstring("anviaj"))
