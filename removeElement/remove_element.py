from itertools import count
from typing import List

nums = [3,2,2,3]
#nums = [0,1,2,2,3,0,4,2]
val = 3
#val = 2

def removeElement(nums: List[int], val: int) -> list[int]:
    for i in range(0, nums.count(val)):
        nums.remove(val)

    return nums

print(removeElement(nums, val))