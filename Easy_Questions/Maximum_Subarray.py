class Soluation:
    def maxSubArray(self, nums : List[int]) -> int:
        masSub = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n 
        maxSub = max(maxSub, currSum)

        return masSub
 
list1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Soluation()
obj.maxSubArray(list1)