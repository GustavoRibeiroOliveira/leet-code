class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        prev_max = float("-inf")
        curr_max = nums[0]
        curr_min = nums[0]
        set_bits = nums[0].bit_count()

        for i in range(1, len(nums)):
            if set_bits == nums[i].bit_count():
                curr_max = max(curr_max, nums[i])
                curr_min = min(curr_min, nums[i])
            else:
                if curr_min < prev_max:
                    return False

                prev_max = curr_max
                set_bits = nums[i].bit_count()
                curr_min = nums[i]
                curr_max = nums[i]

        return curr_min > prev_max


teste = Solution()
print(teste.canSortArray(nums=[8, 4, 2, 30, 15]))
