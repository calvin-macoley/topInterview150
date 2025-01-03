from typing import List

nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums: List[int], val: int) -> list[int]:
    for i in range(0, len(nums) - 1):
        if nums[i] == val:
            nums.remove(val)

    return nums

print(removeElement(nums, val))