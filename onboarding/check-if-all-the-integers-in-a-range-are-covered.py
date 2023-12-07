class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        st  = set()

        for a,b in ranges:
            rl = max(left,a)
            rr = min(right,b)

            for i in range(rl,rr+1):
                st.add(i)
        

        return len(st)== (right-left+1)
        


        