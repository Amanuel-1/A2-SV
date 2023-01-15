/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let ss =[];
    let m={
         "{":"}",
          "[":"]",
          "(":")"
    };
 
    
     for(n of s){
       if(["{","[","("].includes(n)){
         ss.push(n)
         console.log(m[n])
       }
       else{
         if(m[ss[ss.length-1]] != n ){
           return false ;
 
         }
         ss.pop()
       }
 
     }
     return (ss.length)?false:true; ;
 };