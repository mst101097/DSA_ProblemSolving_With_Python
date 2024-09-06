from typing import List

class Soluation:
    def mergeSortArray(self, nums1: List[int],m : int, nums2:List[int], n:int) -> None:

        # last index of Nums
        last =  m+n -1

        # merge in Reverse order

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            
            last -= 1
        
        # fill nums1 with the leftover nums2 elements

        while n > 0:
            nums1 [last] = nums2[n]
            n, last =  n - 1, last - 1
             
        print(nums1)

obj = Soluation()
nums1 = [1,2,3,0,0,0]
m = 3
n = 3 
nums2 = [2,5,6]
obj.mergeSortArray(nums1,m,nums2,n)