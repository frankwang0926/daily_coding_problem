'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

# O(N^2)
def addUptok(list, k):
    length = len(list)
    for i in range(length):
        for j in range(i+1, length):
            if (list[i] + list[j]) == k:
                return True
    return False

# O(N)
def addUptok_set(list, k):
    seen = set()
    for num in list:
        # lookup of set: O(1)
        if k - num in seen:
            return True
        seen.add(num) 
    return False

# Yet another solution involves sorting the list. 
# We can then iterate through the list and run a binary search on k - lst[i]. 
# Since we run binary search on N elements, this would take O(N*log N) with O(1) space.

from bisect import bisect_left

def binary_search(list, target):
    index = bisect_left(list, target)

    if 0 <= index < len(list) and list[index] == target:
        return index

    return -1

def addUptok_binarySearch(list, k):
    list.sort()
    length = len(list)

    for i in range(length):
        target = k - list[i]
        index = binary_search(list, target)

        if index == -1:
            continue
        elif index != i:
            return True
        elif index + 1 < length and list[index + 1] == target:
            return True
        elif index - 1 >= 0 and list[index - 1] == target:
            return True

    return False
    
print(addUptok_set([10,15,3,7], 17))
print(addUptok_set([11,15,3,7], 17))
print(addUptok_set([10,15,3,7,2], 17))
print(addUptok_set([10,15,3,7], 16))

print(addUptok_binarySearch([10,15,3,7], 17))
print(addUptok_binarySearch([11,15,3,7], 17))
print(addUptok_binarySearch([10,15,3,7,2], 17))
print(addUptok_binarySearch([10,15,3,7], 16))