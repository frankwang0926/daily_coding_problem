'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

# with division
# O(N^2)
def productArray1(arr):
    product = 1
    new_arr = []
    for num in arr:
        product *= num

    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr.append(int(product / arr[i]))
        else:
            new_product = 1
            for j in range(len(arr)):
                if j != i:
                    new_product *= arr[j]
            new_arr.append(new_product)

    return new_arr

# without division
# O(N^2)
def productArray2(arr):
    new_arr = []

    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if j != i:
                product *= arr[j]
        new_arr.append(product)

    return new_arr

# without division
def prefix_products(arr):
    new_arr = []
    for num in arr:
        if new_arr:
            new_arr.append(new_arr[-1]*num)
        # if new_arr is empty
        else:
            new_arr.append(num)
    return new_arr

def suffix_products(arr):
    new_arr = []
    # reversed(sequ): returns an iterator that accesses the given sequence in the reverse order.
    for num in reversed(arr):
        if new_arr:
            new_arr.append(new_arr[-1]*num)
        # if new_arr is empty
        else:
            new_arr.append(num)
    return list(reversed(new_arr))

def productArray3(arr):
    new_arr = []
    prefix = prefix_products(arr)
    suffix = suffix_products(arr)
    for i in range(len(arr)):
        if i == 0:
            new_arr.append(suffix[i+1])
        elif i == len(arr) - 1:
            new_arr.append(prefix[i-1])
        else:
            new_arr.append(prefix[i-1]*suffix[i+1])
    return new_arr
    
print(productArray1([1,2,3,4,5]))
print(productArray2([1,2,3,4,5]))
print(productArray3([1,2,3,4,5]))              
print(productArray1([0,2,3,4,5]))   
print(productArray2([0,2,3,4,5]))  
print(productArray3([0,2,3,4,5])) 

