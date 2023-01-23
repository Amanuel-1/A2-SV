/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    // let func = (x)=>{

    // }
    if(n==0){
        return false;
    }
    if(n==1){
        return true ;
    }
    if(n%4!=0){
       return false
    }
    else{
        return  isPowerOfFour(n/4) ;
    }

};
