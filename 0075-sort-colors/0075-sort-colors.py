class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = len(nums)
        zeros, twos = 0, count - 1
        curr = 0

        # [0, 0, 2, 1, 1, 2]


        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        while curr <= twos:
            if nums[curr] == 0:
                swap(curr, zeros)
                zeros += 1
            elif nums[curr] == 2:
                swap(curr, twos)
                twos -= 1
                curr -= 1
            curr += 1
        