from typing import List
class Solution: 
  def twoSum(self, numbers: List[int], target: int) -> list:
    left, right = 0, len(numbers)-1
    while left < right: 
      curSum = numbers[left] + numbers[right]
      if curSum > target:
        right -=1
      elif curSum < target: 
        left +=1
      else: 
        return [left+1, right+1]
    return []

numbers = [2,7,11,15]
target = 9
solution=Solution()
result = solution.twoSum(numbers, target)
print("Indices of numbers that add up to the target: ", result)
# Output: Indices of numbers that add up to the target:  [1, 2]
# Time complexity: O(n)
# Space complexity: O(1)
# Approach: Two pointer approach
# The two pointer approach is a technique where you use two pointers to traverse a list or array.
# The two pointers are initialized at the start and end of the list or array.
