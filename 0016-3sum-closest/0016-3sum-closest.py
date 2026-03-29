class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = len(nums)
        closest, min_diff = float("inf"), float("inf")

        for i in range(count):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, count - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return target
                diff = abs(total - target)
                if min_diff > diff:
                    min_diff = diff
                    closest = total
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
        return closest