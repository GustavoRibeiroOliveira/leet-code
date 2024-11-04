class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        words = sentence.split(" ")
        for index in range(len(words) - 1):
            if words[index][-1] != words[index + 1][0]:
                return False
        return True


teste = Solution()
print(teste.isCircularSentence(sentence="Leetcode is cool"))
