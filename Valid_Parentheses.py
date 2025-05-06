class ParenthesesValidator: 
    def __init__(self,s):
      self.s = s #store the input string

    def is_valid(self):
       stack = []

       bracket_map = {')':'(', '}': '{', ']': '['} #mapping of closing to opening brackets)'}

       for char in self.s: 
            if char in bracket_map:
                top=stack.pop() if stack else '#'
                if bracket_map[char]!=top:
                    return False
            else:
                stack.append(char)
       return not stack
    
validator = ParenthesesValidator("()[]{}")
print(validator.is_valid()) #Output: True

    
  