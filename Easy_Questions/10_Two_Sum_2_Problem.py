class Soluation:
    # This is Two Sum 2nd type problem Where we get sorted element in Array or Index start with 1 not 0.
    def twoSum(self, numbers: list[int], target: int ) -> list[int]:
        leftPointer , rightPointer = 0, len(numbers) -1

        while leftPointer < rightPointer:
            curSum = numbers[leftPointer] + numbers [rightPointer]

            if curSum > target:
                rightPointer -= 1
            elif curSum < target:
                leftPointer += 1
            else:
                return [leftPointer + 1, rightPointer + 1]

list1 = [2, 7, 11, 15]
target = 9
obj = Soluation()
result = obj.twoSum(list1, target)
print(result)