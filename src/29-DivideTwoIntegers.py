class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # This solution exceeds time limit
        # quotient = 0
        # is_dividend_negative = dividend < 0
        # is_divisor_negative = divisor < 0
        # dividend = abs(dividend)
        # divisor = abs(divisor)
        # if divisor == 1:
        #     quotient = dividend
        # else:
        #     while dividend >= divisor:
        #         quotient += 1
        #         dividend -= divisor
        # if (is_dividend_negative and not is_divisor_negative) or (not is_dividend_negative and is_divisor_negative):
        #     if quotient < (-2 ** 31):
        #         return -2 ** 31
        #     return int("-"+str(quotient))
        # if quotient > ((2 ** 31)-1):
        #     return (2 ** 31)-1
        # return quotient
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if abs(divisor) == 1:
            return dividend * divisor

        is_negative = (dividend < 0) ^ (divisor < 0)
        count = 0

        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            x = 1
            base = divisor
            while base <= (dividend >> 1):
                base <<= 1
                x <<= 1
            count += x
            dividend -= base

        return -count if is_negative else count


teste = Solution()
print(teste.divide(dividend=2147483647, divisor=2))
