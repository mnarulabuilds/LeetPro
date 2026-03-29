class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        count = len(nums)
        result = set()
        for i in range(count):
            target = -nums[i]
            j, k = i + 1, count - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    result.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
        return list(result)