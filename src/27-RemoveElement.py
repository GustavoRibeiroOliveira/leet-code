class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        new_list = []
        for num in nums:
            if num != val:
                new_list.append(num)
        length = len(new_list)
        for i in range(length):
            nums[i] = new_list[i]
        return length


teste = Solution()
print(teste.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
