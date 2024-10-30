class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


teste = Solution()
print(teste.twoSum(nums=[2, 7, 11, 15], target=9))
