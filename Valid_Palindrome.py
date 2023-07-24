class Solution:
    def isPalindrome(self, s: str) -> bool:
      string_  = s.lower()
      i,j=0,len(s)-1
      state_ =True
      
      while i<j:
        vi = string_[i]
        vj = string_[j]
        if vi.isalnum() and vj.isalnum():
          if vi!=vj:
            state_ = False
            break
          else:
            i+=1
            j-=1
        else:
          if not (vi.isalnum()) :
            i+=1
          if not (vj.isalnum()):
            j-=1
        
      return state_
          
