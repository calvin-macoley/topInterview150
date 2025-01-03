from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    # Start merging from the end
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Copy any remaining elements from nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


# Test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))