/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
   

    let ss =s.split(" ")
    let last1,last2,temp;
    
    for(let i = 0 ; i<ss.length ;i++){
         
         //console.log(typeof(last1))
         for(let j=i ;j<ss.length ; j++){
              last1 =parseInt((ss[i])[ss[i].length-1])
              last2 =parseInt((ss[j])[ss[j].length-1]);
              if(last1>last2){
                   temp = (ss[i]);
                   ss[i] = ss[j];
                   ss[j] =temp ;
              }
              
         }
    
    }
     ss =ss.map((e)=>{
         let sp = e.split('');
         sp.pop();
        
     
      return sp.join('')
       
    })
    return ss.join(' ')
    };
    