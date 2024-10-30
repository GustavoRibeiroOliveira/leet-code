class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == target:
                    return total

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total > target:
                    k -= 1
                else:
                    j += 1

        return closest_sum


teste = Solution()
print(teste.threeSumClosest(nums=[-1,2,1,-4], target=1))
