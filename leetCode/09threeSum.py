class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        i = 0
        while i < len(nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    continue
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1 
            i += 1
        return result

sol = Solution()
n = [-1,0,1,2,-1,-4]
print(sol.threeSum(n))
n = [-2,0,0,2,2]
print(sol.threeSum(n))
