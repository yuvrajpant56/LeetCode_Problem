class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

def printList(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create linked list 1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3
# Create linked list 2
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6



merged_list = mergeTwoLists(node1, node4)
print("Merged sorted linked list: ")
printList(merged_list)
# Output: