from typing import List
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    maxSum = nums[0]
    curSum=0

    for n in nums: 
      if curSum < 0:
        curSum = 0
      curSum +=n
      maxSum = max(maxSum, curSum)
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
result = solution.maxSubArray(nums)
print("Maximum Subarray sum: ", result)
# Output: Maximum Subarray sum:  6