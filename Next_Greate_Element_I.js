/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    let i,val=[];
    
    val.length = nums1.length ;
    val.fill(-1);
    nums1.forEach((n,id)=>{
        i = nums2.indexOf(n)+1;
        while(i<nums2.length){
            if(nums2[i]>n){
                val[id] = nums2[i]
                break ;
            }
            i++;
        }
    })
    return val;
};
