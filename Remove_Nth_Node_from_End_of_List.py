class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    print("ListNode initialized with value:", self.val)


def removeNthFromEnd(head, n):
  dummy = ListNode(None, head)
  slow = dummy
  fast = dummy
  print("Dummy node initialized with value:", dummy.val)
  print("Slow node initialized with value:", slow.val)
  print("Fast node initialized with value:", fast.val)
  print("Head node initialized with value:", head.val)

  for _ in range(n+1):
    fast = fast.next

  while fast: 
    fast = fast.next
    slow = slow.next

  slow.next = slow.next.next

  return dummy.next 








a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b; b.next = c; c.next = d; d.next = e; 

result = removeNthFromEnd(a, 2)

while result: 
  print(result.val, end=" ->")
  result = result.next


