from typing import List

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> list[int]:
    for i in nums2:
        nums1.append(i)

    for x in range (0, len(nums1)):
        for y in range (x + 1, len(nums1)):
            if nums1[x] >= nums1[y]:
                nums1[x],  nums1[y] =  nums1[y],  nums1[x]

    pop_number(nums1)

    return nums1

def pop_number(nums1: List[int]):
    cpt = 0
    while nums1[cpt] == 0:
        nums1.pop(cpt)

    return nums1

print(merge(nums1, m, nums2, n))