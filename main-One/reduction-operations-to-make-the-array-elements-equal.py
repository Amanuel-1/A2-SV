class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ind  =  [i for i in range(len(nums))]
        def comp(x,y):
            if x[0]>y[0]:
                return -1
            elif x[0]==y[0]:
                if x[1]>y[1]:
                    return 1
                else:
                    return -1
            else:
                return 1



        # nums  = sorted(zip(nums,ind),key =cmp_to_key(comp))
        # min_ = float('inf')
        mp = defaultdict(int)
        for n in nums:
            mp[n]+=1
        
        nums  = sorted(list(set(nums)),reverse=True)
        total  =0
        for i in range(len(nums)-1):
            total+=mp[nums[i]]
            mp[nums[i+1]]+=mp[nums[i]]

    

        return total

