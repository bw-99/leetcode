class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for cursor in range(len(nums)):
            if nums[cursor] == val:
                for idx in range(len(nums)-1, cursor, -1):
                    if nums[idx] != val:
                        nums[cursor], nums[idx] = nums[idx], nums[cursor]
                        k+=1
                        break
            else:
                k+=1
        return k