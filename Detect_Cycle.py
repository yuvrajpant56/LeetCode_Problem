class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    


def hasCycle(head):
  slow = head
  fast = head

  while fast and fast.next: 
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True
  
  return False

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = None

print(hasCycle(a)) # Expected Output: True
