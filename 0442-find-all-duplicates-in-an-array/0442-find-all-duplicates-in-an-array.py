class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        count = len(nums)
        for idx in range(count):
            new_idx = abs(nums[idx]) - 1
            if nums[new_idx] < 0:
                output.append(abs(nums[idx]))
            nums[new_idx] = -nums[new_idx]
        return output