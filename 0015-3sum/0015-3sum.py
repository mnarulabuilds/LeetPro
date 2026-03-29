class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        count = len(nums)
        result = []

        for i in range(count):
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, count - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
        return result