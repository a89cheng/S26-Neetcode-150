# Completed May, 15 2026 | 48 minutes

class TimeMap:
   def __init__(self):
       self.keys = dict()

   def set(self, key: str, value: str, timestamp: int) -> None:
       if key not in self.keys:
           self.keys[key] = [(timestamp,value)]
       else:
           self.keys[key].append((timestamp,value))

   def get(self, key: str, timestamp: int) -> str:
       if key in self.keys:
           left = 0
           right = len(self.keys[key]) - 1
           value = ""

           #Needs to be <= to check final value
           while left <= right:
               mid = (left + right) // 2
               if self.keys[key][mid][0] <= timestamp:
                   value = self.keys[key][mid][1]
                   left = mid + 1
               else:
                   right = mid - 1

           return value
       return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
