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
var middleNode = function(head) {
    let trav =head ,count=0 ,head2;
    
    while(trav!=null){
        count++;
        trav =trav.next ;

    }
    trav =head ;
    console.log(parseInt(count/2))
for(let i =0 ; i<parseInt(count/2) ; i++){
    trav =trav.next ;
}

return trav ;

    
};