/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    let i=0;
      let j=piles.length-1;
      let sum =0;
      piles.sort((a,b)=>{return a-b    })
       while(i<j){
        console.log(piles[i],piles[j])
        sum+=piles[j-1]
          j-=2;
          i++;
      }
      
      return sum
  };