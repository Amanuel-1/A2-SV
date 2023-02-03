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
var reverseList = function(head) {
    if(head ==null || head.next==null){
        return  head
    }
  let t1 = null ,t2=head
  let temp=t2.next
  while(t2.next){
     t2.next = t1;
///    console.log(t2.val)
    t1 = t2
    t2 =temp
    temp = temp.next
  }
  t2.next=t1
return t2
};
