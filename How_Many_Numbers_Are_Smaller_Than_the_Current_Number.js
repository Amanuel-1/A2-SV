/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let counter=0,result =[];

    for(let i=0;i<nums.length ; i++){
        counter =0;
        for(let j=0;j<nums.length;j++){
            if(nums[j]<nums[i] && i!=j){
                counter ++ ;
            }
        }
        result.push(counter);
        
    }
    return result;
};

