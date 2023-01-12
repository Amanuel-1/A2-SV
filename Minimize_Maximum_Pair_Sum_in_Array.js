/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {

    nums.sort((a,b)=>{return a-b  })
    
    let i=0 ;j=nums.length-1;
    let maxsum =0;
  while(i<j){

      maxsum = Math.max(maxsum,nums[i]+nums[j])

      i++;
      j--;
  }
  return maxsum;
};