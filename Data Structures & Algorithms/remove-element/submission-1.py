class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #nums = int(input())
        #val = input("Value to remove: ")

        i = 0
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            

        # "k =", k, "nums =", nums

        return k
        
