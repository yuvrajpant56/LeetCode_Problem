class solution:
    def largestRectangleArea(self, heights : list[int]) -> int:
        # Initialize a stack to keep track of the indices of the bars
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            # while the current bar is lower than the bar at the top of the stack 
            while stack and stack[-1][1] > h:
             
                # pop the top bar from the stack
                index, height = stack.pop()
                # calculate the area with the popped bar as the smallest bar
                max_area = max(max_area, height * (i - index))
                start = index
            # push the current bar onto the stack
            stack.append((start,h))
          # calculate the area for the remaining bars in the stack
        for index, h in stack:
            max_area = max(max_area, h * (len(heights) - index))
        return max_area
    
# Example usage
heights = [2,1,5,6,2,3]
s = solution()
print(s.largestRectangleArea(heights))  # Output: 10
# Example usage
heights = [2,4]
s = solution()
print(s.largestRectangleArea(heights))  # Output: 4


            