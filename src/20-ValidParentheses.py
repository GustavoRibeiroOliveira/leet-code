class Solution(object):
    def isValid(self, s):
        close_order = []
        for char in s:
            if char in ("(", "[", "{"):
                close_order.append(char)
            else:
                if (
                    char == ")"
                    and "(" in close_order
                    and close_order[-1] == "("
                ):
                    close_order.pop()
                elif (
                    char == "]"
                    and "[" in close_order
                    and close_order[-1] == "["
                ):
                    close_order.pop()
                elif (
                    char == "}"
                    and "{" in close_order
                    and close_order[-1] == "{"
                ):
                    close_order.pop()
                else:
                    return False
        if close_order:
            return False
        return True


teste = Solution()
print(teste.isValid(s="(([]){})"))  # Expected True
