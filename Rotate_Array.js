/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
  //  let arr = nums.splice(0,k+1) ; 
  k = k%(nums.length)
let temp = nums.splice(nums.length-k).reverse() ; 
for(n of temp){
    nums.unshift(n)
}
};
