# /**
#  * @param {number[]} nums
#  * @return {number}
#  */
# var missingNumber = function(nums) {
#     nums.sort((a,b)=>{
#         return a-b;
#     });
#     let i = 0  ; 
#   while(i<nums.length){
#       if(nums[i]!=i){
#           return i ;
#       }
#       i++;
#   }
#   return i ;
# }
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      nums = sorted(nums)
      i=0
      while i<len(nums):
        if nums[i]!=i:
          return i
        i+=1
      return i
      
