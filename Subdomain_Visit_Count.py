class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
      mp={}
      result=[]
      def store(string,count):
        j =len(string)-1
        while j>=-1:
          if string[j] =="." or j ==-1:
            trimmed = string[j+1:]
            
            if trimmed in mp:
              mp[trimmed] +=count
            else:
              mp[trimmed]=count
          j-=1
        
      for ind in cpdomains:
        count,string = ind.split()
        store(string,int(count))
        print(count +" +"+ string)
      
      for key in mp:
        result.append(str(mp[key])+ " "+ key)
      return result

        
      
