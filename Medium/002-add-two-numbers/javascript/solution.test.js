const { ListNode, addTwoNumbers } = require('./solution')

const toArray = (listNode) => {
    let output = []
    while(listNode !== null) {
        output.push(listNode.val)
        listNode = listNode.next
    } 
    return output
}

const toLinkedList = (array) => {
    let linkedList = new ListNode(0)
    let tail = linkedList
    array.forEach(element => {
        const newNode = new ListNode(element)
        tail.next = newNode
        tail = tail.next
    });
    return linkedList.next
}

describe('Add Two Numbers - Javascript', () => {
    test('Standard case: 342 + 465 = 807', () => {
        l1 = toLinkedList([2, 4, 3])
        l2 = toLinkedList([5, 6, 4])
        result = addTwoNumbers(l1, l2)
        expect(toArray(result)).toEqual([7, 0, 8]);
    });
    test('One number is longer than the other', () => {
        l1 = toLinkedList([9, 9])
        l2 = toLinkedList([1])
        result = addTwoNumbers(l1, l2)
        expect(toArray(result)).toEqual([0, 0, 1]);
    });
    test('One number is longer than the other', () => {
        l1 = toLinkedList([5])
        l2 = toLinkedList([5])
        result = addTwoNumbers(l1, l2)
        expect(toArray(result)).toEqual([0, 1]);
    });
})