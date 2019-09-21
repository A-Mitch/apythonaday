# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class twoSumSols:

    # This will go through a list and test to see what integers will equal the to the target
    # The sum = nums[i]+nums[j]
    # Runtime: O(n^2) or 5292 ms - 5492 ms

    def bruteForce(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

    # Look for the complement of my subtracted value and match them
    # Runtime: O(n) or 56 ms
    def quickerSol(nums: List[int], target: int) -> List[int]:

        complDict = dict()
        for index,value in enumerate(nums):
            # mMy num is the index that I am on
            num = nums[index]
            # The complement is the target - the value at that index
            compls = target - nums[index]
            # If we find that the current num is inside the dictionary then we find the value stored and return that dict index 
            # and the for loop index
            if num in complDict:
                return [complDict[num],index]
            else:
                complDict[compls] = index

    

