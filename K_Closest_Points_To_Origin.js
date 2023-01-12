/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    let result =[]
    points.sort((a,b)=>{
         return (((a[0])**2 +(a[1])**2 ) >((b[0])**2 +(b[1])**2))?1:-1;
        //return (a[0]-a[1] > b[0]-b[1])?1:-1;
          }) 

          let i=0 ; 
          while(i<k){
             result.push(points[i])
             i++;
          }
    return result
 };
