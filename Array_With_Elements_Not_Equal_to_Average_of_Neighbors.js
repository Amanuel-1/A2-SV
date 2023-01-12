/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    nums.sort((a,b)=>{
     return a-b;
    }) ;

    let len = nums.length;
    let even=[],odd=[]
    let mid =(len%2==0)? (nums[parseInt(len/2)]+nums[parseInt(len/2) -1])/2 : (nums[parseInt(len/2)])
    console.log(mid)



    for(n of nums){
     if(n<mid){
       odd.push(n)
       
     }
     else{
       even.push(n)
     }
    }
    console.log(even)
    console.log(odd)


    for(let i=0;i<even.length;i++){
     nums[i*2] =even[i]
    }
    for(let i=0;i<odd.length;i++){
     nums[i*2 +1]  =odd[i]
    }
    return nums
   };