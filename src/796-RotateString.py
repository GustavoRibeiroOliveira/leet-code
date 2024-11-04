class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        length = len(s)
        if length != len(goal):
            return False
        if s == goal:
            return True
        for index in range(length):
            s = s[1:length] + s[0]
            if s == goal:
                return True
        return False


teste = Solution()
print(teste.rotateString(s="abcde", goal="abced"))
