class Solution:
    def arrayPairSum(self, nums:list[int])->int:
        nums.sort()
        return sum(nums[::2])

sol = Solution()
n=[1,4,3,2]
print(sol.arrayPairSum(n)
