/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function(head) {
    let t = head,len = 0,mx=0 ;
    while(t){
        len ++
        t = t.next;
    }
    t = head ;
    for(let i = 0 ; i<(len/2) ; i++){
        t =t.next
    }
  let t1 = null ,t2=t,t3 = t2.next ;
    while(t3){
        t2.next = t1 ; 
        t1 =t2 ; 
        t2 = t3 ; 
        t3 = t3.next
    }
t2.next = t1 ;


t1 =head , t3 =t2 ;//instead of asigning another pointers
while(t3){
   mx  = Math.max(mx,t1.val+t3.val)
   t3 = t3.next ;
   t1 = t1.next
}
return mx
};
