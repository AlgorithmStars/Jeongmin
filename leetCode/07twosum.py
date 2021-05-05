import bisect

class Solution:
    def twoSum(self, nums:list[int], target:int) ->list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
        return None

#        sortedNums = sorted(nums)
#        print(sortedNums)
#        for a in range(len(sortedNums)):
#            b = bisect.bisect_left(sortedNums, target - sortedNums[a])
#            if a == b or b == len(sortedNums): # invalid
#                continue
#            print(a,b)
#            if sortedNums[a] + sortedNums[b] == target:
#                indexA = nums.index(sortedNums[a])
#                indexB = nums.index(sortedNums[b])
#                if indexA == indexB:
#                    indexB = nums.index(sortedNums[b], indexA+1)
#                return indexA, indexB
#        return None # invalid

sol = Solution()
n=[-1,-2,-3,-4,-5]
t=-8
print(sol.twoSum(n, t))
