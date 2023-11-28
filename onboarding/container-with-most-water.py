class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        mxarea = -float('inf')

        while i<j:
            minh  = min(height[i],height[j])

            mxarea = max(mxarea,(j-i)*minh)

            if minh == height[i]:
                i+=1
            else:
                j-=1

        return mxarea
