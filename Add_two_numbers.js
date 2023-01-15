/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */var addTwoNumbers = function(l1, l2) {
    let t1 = l1;
    let t2 =l2 ;
  
     
     let rem =0 ,val1,val2;
     let degit;
     let sum =[];
     let result =new ListNode(0); 
     let r =result;
     if(t1 && !t2){return t1}
    if(!t1 && t2){return t2}
     while(t1 || t2 || rem){
        // val1 =(trav1=null)?0:trav1.val
        // val2 =(trav2.null)?0:trav2.val
          val1 =t1?t1.val:0 ;
          val2 =t2?t2.val:0;
          digit = (val1 + val2+rem)%10 ;
      rem = (digit== (val1 + val2+rem))?0:1;
  
          sum.push(digit)
          r.next = new ListNode(digit)
  
          r =r.next ;
          t1 = t1?t1.next:null;
          t2 =t2?t2.next:null;
          
     }
     
     r.next =(rem==0)?r.next:new ListNode(rem)
    result =result.next
   
    return result
  };