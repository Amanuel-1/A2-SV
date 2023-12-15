class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower,upper,piv =[],[],[]

        for n in nums:
            if n<pivot:
                lower.append(n)
            elif n>pivot:
                upper.append(n)
            else:
                piv.append(n)
        
        answer=lower+piv+upper
        return answer