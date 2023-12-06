class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps  = 0 

        max_ =capacity
        for i in range(len(plants)-1):
            capacity-=(plants[i])
            if plants[i+1]>capacity:
                steps+= (i+1)*2
                capacity =max_
            
            steps+=1


        return steps+1
        