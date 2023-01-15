var MinStack = function() {
    this.stack =[] ;
     
 };
 
 /** 
  * @param {number} val
  * @return {void}
  */
 MinStack.prototype.push = function(val) {
     this.stack.push(val);
 };
 
 /**
  * @return {void}
  */
 MinStack.prototype.pop = function() {
     this.stack.pop();
 };
 
 /**
  * @return {number}
  */
 MinStack.prototype.top = function() {
     return this.stack[this.stack.length -1]
 };
 
 /**
  * @return {number}
  */
 MinStack.prototype.getMin = function() {
     let minim =this.stack[0] ;
     for(n of this.stack){
         minim  = Math.min(minim , n)
     }
     return minim ;
 };
 
 /** 
  * Your MinStack object will be instantiated and called as such:
  * var obj = new MinStack()
  * obj.push(val)
  * obj.pop()
  * var param_3 = obj.top()
  * var param_4 = obj.getMin()
  */