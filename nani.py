def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el
     return min_number
nums1 = [1, 9, 4, 99, 73, 21]
min1 = minimal(nums1)

nums2 = [2.4, 8.1, 3.5]
min2 = minimal(nums2)

if min1 < min2