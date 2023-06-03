class Soluation:
    def maxSubArray(self, nums : list[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n 
            maxSub = max(maxSub, currSum)

        return maxSub
 
list1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Soluation()
returnSubArray = obj.maxSubArray(list1)
print(returnSubArray)
