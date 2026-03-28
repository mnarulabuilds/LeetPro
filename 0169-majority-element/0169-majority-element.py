class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        n = len(nums)
        if n == 0:
            return -1
        major = nums[0]
        for i in range(1, n):
            if nums[i] == major:
                count += 1
            elif count == 0:
                major = nums[i]
                count = 1
            else:
                count -= 1
        return major