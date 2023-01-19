/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
  intervals.sort((a,b)=>{return a[0]-b[0]})
   
    let count =1, min,max ;

    for(let i=0;i<intervals.length-1;){
      max =Math.max(intervals[i][1],intervals[i+1][1])
        if(intervals[i][1]>=intervals[i+1][0]){
            intervals.splice(i,2,[intervals[i][0],max])

             i--
        }
        else{
            count++
        }
        i++;
    }
return intervals
};
