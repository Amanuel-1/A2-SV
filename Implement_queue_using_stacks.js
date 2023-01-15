var MyQueue = function() {
    this.que =[];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.que.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
   return this.que.splice(0,1);
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    return this.que[0]
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return (this.que.length==0)?true:false
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */