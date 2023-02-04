/**
 * @param {number} k
 */
 let size ;

var MyCircularDeque = function(k) {
    size = k;
    this.deq=[];

    
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function(value) {
    if(this.deq.length<size){
        this.deq.unshift(value)
        return true;
    }
    return false;
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function(value) {
    if(this.deq.length<size){
        this.deq.push(value);
        return true;
    }
    return false;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function() {
    if(this.deq.length){
        this.deq.shift();
        return true;
    }
    return false;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function() {
    if(this.deq.length){
        this.deq.pop();
        return true;

    }
    return false;
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function() {
    if(this.deq.length){
        return this.deq[0]
    }
    return -1 ;
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function() {
    if(this.deq.length){
        return this.deq[this.deq.length-1];
    }
    return -1
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function() {
    return this.deq.length ==0
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function() {
    return this.deq.length==size;
};

/** 
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */
