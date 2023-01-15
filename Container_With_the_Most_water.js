/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let area=0;
    let minheight,length;

   /* for(let i=0;i<height.length;i++){
        for(let j=height.length-1;j>i;j--){
            minheight =Math.min(height[i],height[j]);
            length = Math.abs(i-j);
            area =(minheight*length >area)?minheight*length:area;
           // console.log(area)
        }
    }
    */
    let i=0;j=height.length-1;
    while(i<j){
         minheight =Math.min(height[i],height[j]);
         length = Math.abs(i-j);
         area =(minheight*length >area)?minheight*length:area;
         if(height[i]<height[j]){
             i++
         }
         else{
             j--
         }
    }
return area;
};