# Completed April, 25 2026 | 45 minutes

class Solution:
   def search(self, nums: List[int], target: int) -> int:
       n = len(nums)
       left = 0
       right = n-1
       mid = (left + right) // 2

       while left < right:
           mid = (left + right) // 2

           if nums[mid] == target:
               return mid

           # There will always be a "sorted" side
           if nums[left] <= nums[mid]:
               #left side is sorted
               if nums[left] <= target <= nums[mid]:
                   right = mid
               else:
                   left = mid+1
           elif nums[mid] <= nums[right]:
               #right side is sorted
               if nums[mid] <= target <= nums[right]:
                   left = mid
               else:
                   right = mid-1

       #should exit when they are the same
       if nums[left] == target:
           return left
       else:
           return -1