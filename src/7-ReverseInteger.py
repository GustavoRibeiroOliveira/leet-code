class Solution(object):
    def reverse(self, x):
        upper_limit = (2**31) - 1
        lower_limit = 2**31

        if x < 0:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            if int(x) > lower_limit:
                return 0
            return int("-" + x)
        x = str(x)
        x = x[::-1]

        if int(x) > upper_limit:
            return 0
        return int(x)


teste = Solution()
print(teste.reverse(-2147483648))
