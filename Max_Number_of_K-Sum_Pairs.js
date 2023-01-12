/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    let counter=0
   let i=0;
   let j=nums.length-1;
   nums.sort((a,b)=>{
       return a-b
   })

   while(i<j){
       if(nums[i]+nums[j] ==k){
         
          i++;
          j--;
            counter++;
       }
       else if(nums[i]+nums[j]>k){
           j--
       }
       else{
           i++;
       }
   }
    console.log(nums)
    return counter
};