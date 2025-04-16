class ListNode:
  def __init__(self, val=0, next=None):
    self.val =val
    self.next = next

def reverseList(head):
  prev = None
  curr = head

  while curr: 
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
  return prev

# Example usage / quick test
if __name__ == "__main__":
  # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  # Reversing the linked list
  reversed_head = reverseList(head)
  # Printing the reversed linked list
  current = reversed_head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")
# Expected Output: 5 -> 4 -> 3 -> 2 -> 1 -> None