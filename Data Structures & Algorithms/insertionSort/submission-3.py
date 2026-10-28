# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs) # gets the lentgth of the list
        res = [] # stores the sorted list
        for i in range(n): # goes through every item in the list
            j = i - 1 #The index will be less to check the item before that
            while j >= 0 and pairs[j].key > pairs[j + 1].key: # Keep on looping iff j is greater or equal to 0 so it will not cross the outerbounds and until there are swaps to be made
                temp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = temp # swaps them
                j = j - 1 #goes to the previus item and checks
            res.append(pairs[:]) #appednds the sorted elements
        return res #returms the sorted items