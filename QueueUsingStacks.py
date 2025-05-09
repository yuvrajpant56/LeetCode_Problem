class MyQueue:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []

  def push(self,x):
    self.in_stack.append(x)

  def pop(self):
    self.move_in_to_out()
    return self.out_stack.pop()
  
  def peek(self):
    self.move_in_to_out()
    return self.out_stack[-1]
  
  def empty(self):
    return not self.in_stack and not self.out_stack
  
  def move_in_to_out(self):
    if not self.out_stack: 
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek()) #Output: 1
print(q.pop())  #Output: 1
print(q.empty()) #Output: False
