/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
var checkArithmeticSubarrays = function(nums, l, r) {
    let query = (i)=>{
        let queried=[]
        for(let k=l[i]; k<=r[i];k++){
            queried.push(nums[k])
        }
        return queried
    }
       let check =(arr)=>{
        arr.sort((a,b)=>{
            return a-b;
        })
        let d =arr[1]-arr[0],c=0;
        for(let i=0;i<arr.length-1;i++){
            if(arr[i+1]-arr[i] !=d){
               return false
            }
        }
        return true;
    }
    let answer =[]
    for(let i=0;i<l.length;i++){
        let arr =query(i)
        answer.push(check(arr))
    }


return answer
};


console.log(checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))