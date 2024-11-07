class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        answer = 0

        for index in range(32):
            count = 0
            for candidate in candidates:
                if candidate & (1 << index):
                    count += 1
            answer = max(answer, count)
        return answer


teste = Solution()
print(teste.largestCombination(candidates = [16,17,71,62,12,24,14]))