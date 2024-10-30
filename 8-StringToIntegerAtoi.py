class Solution(object):
    def myAtoi(self, s):
        is_positive = False
        is_negative = False
        non_zero_found = False
        number_found = False
        string = ""
        upper_limit = (2 ** 31) - 1
        lower_limit = (2 ** 31)
        numbers = "1234567890"

        index = 0
        for char in s:
            if char not in numbers and number_found:
                break
            elif char == "+" and not number_found:
                is_positive = True
                number_found = True
            elif char == "-" and not number_found:
                is_negative = True
                number_found = True
            elif char in numbers:
                number_found = True
                string += char
                if char != "0":
                    non_zero_found = True
            elif char == " " and len(string) == 0:
                pass
            else:
                break

        if len(string) == 0:
            return 0
        if not is_positive and not is_negative:
            if int(string) > upper_limit:
                return int(str(upper_limit))
        if is_positive:
            if int(string) > upper_limit:
                return int("+"+str(upper_limit))
            return int("+"+string)
        if is_negative:
            if int(string) > lower_limit:
                return int("-"+str(lower_limit))
            return int("-"+string)
        return int(string)

teste = Solution()
print(teste.myAtoi("  +  413"))