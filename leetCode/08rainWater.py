class Solution:
    def trap(self, height: list[int]) -> int:

        result = 0

        currentMaximum = 0
        tmp = 0

        for leftBar in height:
            if leftBar >= currentMaximum:
                result +=  tmp

                currentMaximum = leftBar
                tmp = 0
            else:
                tmp += currentMaximum - leftBar

        currentMaximum = 0
        tmp = 0
        for rightBar in height[::-1]:
            if rightBar > currentMaximum:
                result +=  tmp

                currentMaximum = rightBar 
                tmp = 0
            else:
                tmp += currentMaximum - rightBar



        return result


sol = Solution()
h=[0,1,0,2,1,0,1,3,2,1,2,1] # 6
print(sol.trap(h))
h=[4,2,0,3,2,5] # 9
print(sol.trap(h))
