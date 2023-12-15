class UndergroundSystem:

    def __init__(self):
        self.overAllmp = defaultdict(list)
        self.record = defaultdict(list)

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.record[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,time  =  self.record[id]
        if (start,stationName) not in self.overAllmp :
            self.overAllmp[(start,stationName)]=[0,0]
        self.overAllmp[(start,stationName)][0]+=t-time
        self.overAllmp[(start,stationName)][1]+=1
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime ,totalTravel = self.overAllmp[(startStation,endStation)]
        return totalTime/totalTravel

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)