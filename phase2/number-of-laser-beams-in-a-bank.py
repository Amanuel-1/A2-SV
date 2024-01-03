class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i=0
        count =0
        mp=defaultdict(int)
        while i<len(bank) and bank[i].count("1")==0:
            i+=1
        for j in range(i+1,len(bank)):
            devices = bank[j].count("1")

            if devices!=0:
                count+=(bank[i].count("1")*devices)
                i=j
        

        return count



