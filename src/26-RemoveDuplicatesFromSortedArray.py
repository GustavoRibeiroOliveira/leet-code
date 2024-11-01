class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        non_duplicates = set(nums)
        non_duplicates = list(non_duplicates)
        non_duplicates.sort()
        for index in range(len(non_duplicates)):
            nums[index] = non_duplicates[index]
        return len(non_duplicates)


teste = Solution()
print(teste.removeDuplicates(nums=[-1, 0, 0, 0, 0, 3, 3]))
