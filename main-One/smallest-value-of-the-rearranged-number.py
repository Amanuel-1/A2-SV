class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0

        sign  =  num//abs(num)
        def comp(x,y):
            if sign ==-1:
                if x<y:
                    return 1
                else:
                    return -1
            else:
                if x<y:
                    return -1
                else:
                    return 1
            
            
            
        num  = sorted(str(num).replace("-",""),key=cmp_to_key(comp))

        i  = 0
        while num[i]=="0":
            i+=1
        
        num[0],num[i]=num[i],num[0]


        return int("".join(num))*sign

