class HouseRobber: 
  def __init__(self, nums):
    self.nums = nums
  def rob(self)->int:
    nums = self.nums
    n=len(nums)

    # Handle edge cases
    if n == 0:
      return 0
    if n == 1:
      return nums[0]
    
    # Initialize the dp array
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2,n):
      dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    
    return dp[-1]
house_values = [2,7,9,3,1]
house = HouseRobber(house_values)
result = house.rob()
print("Maximum amount that can be robbed: ", result)


# #with space optimization inside the class
# class HouseRobber: 
#   def __init__(self, nums):
#     self.nums = nums
#   def rob(self)->int:
#     nums = self.nums
#     n=len(nums)

#     # Handle edge cases
#     if n == 0:
#       return 0
#     if n == 1:
#       return nums[0]
    
#     # Initialize the dp array
#     prev1 = nums[0]
#     prev2 = max(nums[0], nums[1])

#     for i in range(2,n):
#       current = max(prev2,prev1+nums[i])
#       prev1 = prev2
#       prev2 = current
    
#     return prev2
# house_values = [2,7,9,3,1]
# house = HouseRobber(house_values)
# result = house.rob()  
# print("Maximum amount that can be robbed: ", result)