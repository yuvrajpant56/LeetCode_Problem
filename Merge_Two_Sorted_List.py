class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        print("ListNode initialized with value:", val)
def mergeTwoList(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2: 
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy


# Create Linked list 1
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

# Create linked list 2
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Print the linked lists
print("Linked list 1:")
printList(l1)
print("Linked list 2:")
printList(l2)


# Merge the lists
result = mergeTwoList(l1, l2)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->




