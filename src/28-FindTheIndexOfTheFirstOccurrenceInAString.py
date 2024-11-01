class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle, 0, len(haystack))
        length_needle = len(needle)
        length_haystack = len(haystack)
        if length_needle > length_haystack:
            return -1
        index = 0
        while True:
            if haystack[index : (index + length_needle)] == needle:
                return index
            index += 1
            if index == length_haystack:
                break
        return -1


teste = Solution()
print(teste.strStr(haystack="leetcoaade", needle="aa"))
