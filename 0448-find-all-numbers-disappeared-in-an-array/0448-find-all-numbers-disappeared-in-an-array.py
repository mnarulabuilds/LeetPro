class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        my_set = set()
        n = len(nums)
        result = []

        for num in nums:
            my_set.add(num)

        for num in range(1, n+1):
            if num not in my_set:
                result.append(num)

        return result