/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function (s) {
  let temp= [];
  for (let i of s) {
    if (i !== ")") temp.push(i);
    else {
      let z = [];
     
      while (temp[temp.length - 1] !== "(") {
        z.push(temp.pop());
      
      }
    
      temp.pop();
     
      temp.push(...z);
    }
  }

  return temp.join("");
};
