class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    countS, countT = {}, {}
    for i in range(len(s)):
      if s[i] in countS:
        countS[s[i]] += 1
      else:
        countS[s[i]] = 1
      if t[i] in countT:
        countT[t[i]] += 1
      else:
        countT[t[i]] = 1
    print(countS, countT)
    return countS == countT

s = "anagram"
t = "nagaram"
solution = Solution()
result = solution.isAnagram(s, t)
print("Are the two strings anagrams: ", result)
