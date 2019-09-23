# Done by Alexander Mitchell

# Running time of O(n)
# What does my solution say:
# If a number from my list is inside my hashmap then return true
# If we are at the end of the list and all of our numbers are duplicates then return false
# Else, add that number to my hashmap 


def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for index in range(len(nums)):
            num = nums[index]

            if num in numMap:
                return True
            elif (index == len(nums)) and (num not in numMap):
                return False
            else:
                numMap[num] = index
