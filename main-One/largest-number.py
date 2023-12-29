class Solution:
    def largestNumber(self, nums: List[int]) -> str:


        def comparator(x,y):
            p1,p2  =  str(x)+str(y),str(y)+str(x)
            if p1>p2:
                return -1
            else:
                return 0
            

        nums = sorted(nums,key=cmp_to_key(comparator))
        ans  = "".join([str(n) for n in nums])

        return "0" if int(ans)==0 else ans




