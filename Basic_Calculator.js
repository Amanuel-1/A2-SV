/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    //even through you can just iterate through twice and do it , you are trying to emplement the concept of stack as it is in the progresssheet ;) 
   let nm =[],ans , a,b,o,i = 0 ;
   let op = [];
    s = (s.split(/([-,+,*,/,])/));
   let is_numeric =(str)=>{
   return !isNaN(parseInt(str));
    }
  

while(i<s.length){
   // if(s[i]=='')
    if(is_numeric(s[i])){
        nm.push(parseInt(s[i])) ;
    }
    else if(s[i]=='*' || s[i]=='/')
    {
        a = nm[nm.length-1];
       
        nm.pop();
        b = parseInt(s[i+1]);
      
         o=parseInt(eval(a+s[i]+b));
        nm.push(o);
        i++;
    }
    else if(s[i]=='-'){
        op.push('+')
        s[i+1] = "-"+s[i+1]
    }
    else{
        op.push(s[i])
    }

    i++;
}

while(op.length){
    b = nm[nm.length-1];
    nm.pop();
    a = nm[nm.length-1];
    nm.pop();
    o = op[op.length-1];
    op.pop();
    (o=='-')?nm.push(a-b):nm.push(a+b)
}


return parseInt(nm)
};
