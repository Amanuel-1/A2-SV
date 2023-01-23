/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    let t1 =head ;
    let t2 =(t1)?t1.next:null ;
    let temp;
    while(t1 && t2){
        temp = t1.val;
        t1.val =t2.val;
        t2.val = temp ;

        t1 = (t2)?t2.next:null;
        t2 =(t1)?t1.next:null;
    }
    return head
};
