class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        curr_sum = 0
        count = len(nums)

        for idx in range(k):
            curr_sum += nums[idx]

        max_sum = curr_sum
        for idx in range(k, count):
            curr_sum += nums[idx]
            curr_sum -= nums[idx - k]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k


        