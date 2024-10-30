class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1
        nums3.extend(nums2)
        nums3.sort()
        length = len(nums3)
        metade = int(length / 2)
        if length % 2 == 0:
            return (float(nums3[metade - 1]) + float(nums3[metade])) / 2
        return nums3[metade]


teste = Solution()
print(teste.findMedianSortedArrays([1, 2], [3, 4]))
