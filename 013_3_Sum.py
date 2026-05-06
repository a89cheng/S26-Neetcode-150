# Completed May, 2 2026 | 43 minutes

class Solution:
   def threeSum(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       output = []
       n = len(nums)

       for idx in range(n):
           right = n-1
           left = idx + 1

           target = 0 - nums[idx]

           while left < right:
               if nums[left] + nums[right] == target:
                   if [nums[idx],nums[left],nums[right]] not in output:
                        output.append([nums[idx],nums[left],nums[right]])
                   left += 1
                   right -= 1
               # A very strange idea revolving around sorted!
               elif nums[left] + nums[right] < target:
                   left += 1
               else:
                   right -= 1

       return output