class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
      mp  = defaultdict(int)
      n =  len(fruits)
      i=0
      mxpick  = 0
      for j in range(n):
        mp[fruits[j]]+=1

        if len(mp) >2:
          mp[fruits[i]]-=1
          if mp[fruits[i]]==0:
            del mp[fruits[i]]
          i+=1
        else:
          mxpick = max(mxpick,j-i+1)
      return mxpick





        