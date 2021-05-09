class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1]*len(nums)
            
        pSuffix = [1] * len(nums)
        pSuffix[-1] = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            pSuffix[i] = pSuffix[i+1] * nums[i]

        tmp = nums[0]
        
        answer[0] = pSuffix[1]
        for i in range(1, len(nums)-1):
            answer[i] = pSuffix[i+1] * tmp
            tmp *= nums[i]
        answer[-1] = tmp
        return answer

sol = Solution()
nums = [1,2,3,4] # 24 12 8 6
print(sol.productExceptSelf(nums))
nums = [-1,1,0,-3,3] # 0 0 9 0 0
print(sol.productExceptSelf(nums))
