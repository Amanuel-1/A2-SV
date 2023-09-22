class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        inbus = 0
        ispos =True
        distline =[0]*1001
        maxdest =trips[0][2]
        for i in range(len(trips)):
            print(maxdest,inbus)
            distline[trips[i][1]]+=trips[i][0]
            distline[trips[i][2]]-=trips[i][0]
        for i in distline:
            inbus+=i
            if inbus>capacity:
                ispos =False
                break
        return ispos
        

        
