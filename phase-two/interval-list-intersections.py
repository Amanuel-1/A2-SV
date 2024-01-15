class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i,j =0,0
        answer=[]
        while j<len(secondList) and i<len(firstList):
            x,y  = (max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1]))

            if x<=y:
                answer.append([x,y])
            
            if firstList[i][1]<secondList[j][1]:
                i+=1
            elif firstList[i][1]>secondList[j][1]:
                j+=1
            else:
                i+=1
                j+=1

        

        return answer