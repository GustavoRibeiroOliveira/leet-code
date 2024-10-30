class Solution(object):
    def isPalindrome(self, x):
        str(x)
        y = str(x)[::-1]
        if str(x) == str(y):
            return True
        return False


teste = Solution()
print(teste.isPalindrome("10"))
