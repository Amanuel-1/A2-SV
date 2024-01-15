class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        colors =  defaultdict(int)

        i=0
        min_ = k

        for j in range(len(blocks)):
            
            colors[blocks[j]]+=1
            if j<k-1:
                continue

            min_ = min(min_,(j-i+1)-colors['B'])

            colors[blocks[i]]-=1
            if colors[blocks[i]]==0:
                del colors[blocks[i]]
            i+=1


        return min_

                
        