class Soluation:
    # In this question we need to find the target sum of 2 values in array
    def twoSum(self, nums: list[int], target: int) -> list():
        prevMap = {} #that hold val: index

        for i, n in enumerate(nums):
            diff= target - n
            
            # here the index and value in HashMap
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return

# creating object
S = Soluation()
holdOutput = S.twoSum([2,7,11,15], 9)
print(holdOutput)
