/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
   // popped.reverse();
   let  i = 0 ,j = 0;
   let arr = []
    //console.log(popped)
    for(x of pushed){
        arr.push(x);
       while(arr!=[] && j<pushed.length && arr[arr.length-1] ==popped[j]){
        
               arr.pop();
               j++
          
    
    } 
    }
    console.log(arr)
  return j==popped.length
};
