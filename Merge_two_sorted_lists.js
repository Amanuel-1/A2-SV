/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let t1 =list1 ;
    let t2= list2 ;
    
      let result = new ListNode()
      let trav =result
 if(list1==null && list2!=null){return list2}
 if(list2==null && list1!=null){return list1}
    
     
  
      while(t1!=null || t2!=null){
          
         
  
          if(t2==null ||(t1!=null && t2.val>=t1.val)){
              trav.next =  t1;
              trav =trav.next ;
             t1 = t1.next ;
              
          }
          else{
              trav.next =  t2
              trav =trav.next ;
              t2 =t2.next
              
          }
          
        
          }
 
      
  
  return result.next
  };