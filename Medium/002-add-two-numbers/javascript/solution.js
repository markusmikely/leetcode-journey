/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // Dummy head; to gracefully handle null values
    let anchor = new ListNode(0)
    let curr = anchor;
    let carry = 0; // will hold any values that need to carry over to the next digit being added
    
    // If l1 or l2 are not null, or carry > 0 we still ave vals to add
    while(l1 !== null || l2 !== null || carry > 0) {
        const val1 = l1 ? l1.val : 0
        const val2 = l2 ? l2.val : 0
        const total = val1 + val2 + carry
        carry = Math.floor(total / 10) // the 10s to carry over
        const out = total % 10 // the remainder after removing the 10

        curr.next = new ListNode(out) // create a new node
        curr = curr.next

        l1 = l1 ? l1.next : null
        l2 = l2 ? l2.next : null
    }
    return anchor.next
};

module.exports = { ListNode, addTwoNumbers };
