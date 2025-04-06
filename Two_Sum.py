from typing import List
class Solution:
  def twoSum(self, nums:List[int], target: int)->List[int]:
    #Dictionary to store the value and its index
    prevMap = {}

    for i,n in enumerate(nums):
      #Calculate the complements (the number we need to find)
      diff = target - n

      # if the complement is already in the dictionary, return the result
      if diff in prevMap:
        return [prevMap[diff],i]

      # otherwise, add the current number and its index to the dictionary
      prevMap[n] = i

    # if no solution is found (although the problem guarantess a solution)

    return []

nums=[2,7,11,15]
target = 9

solution = Solution()

result = solution.twoSum(nums, target)

print("Indices of numbers that add up to the target: ", result)

