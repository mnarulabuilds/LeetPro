class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zr = 0
        count = len(nums)
        for curr in range(count):
            if nums[curr] != 0:
                nums[curr], nums[zr] = nums[zr], nums[curr]
                zr += 1 
        return nums
        