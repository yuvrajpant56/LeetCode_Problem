class MinStack: 
  def __init__(self):
    self.main_stack = []
    self.min_stack = []

  def push(self,val):
    self.main_stack.append(val)

    #push the min_stack if empty or val is less than or equal to the last element
    if not self.min_stack or val <=self.min_stack[-1]:
      self.min_stack.append(val)

  def pop(self):
    val = self.main_stack.pop()

    if val == self.min_stack[-1]:
      self.min_stack.pop()

  def top(self):
    return self.main_stack[-1]
  
  def getMin(self):
    return self.min_stack[-1]

s=MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin()) #Output: -3
s.pop()
print(s.top()) #Output: 0
print(s.getMin()) #Output: -2
#Output: -2

  