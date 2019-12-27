'''
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. 
Generalize your function to take in X.
'''

'''
Suppose a staircase with N steps is numbered by N, N-1, N-2, ..., 2, 1, 0
N = 0: {[0]} -> 1
N = 1: {[1, 0]} -> 1
N = 2: {[2, 1, 0], [2, 0]} -> 2
N = 3: {[3, 2, 1, 0], [3, 1, 0], [3, 2, 0]} -> 3

num_ways(3) = num_ways(2) + num_ways(1)

N  # of ways
0     1
1     1
2     2
3     3
4     5

'''

# simple solution with recursion
# not efficient: O(2^N)
def num_ways(N):
    if N == 0 or N == 1:
        return 1
    else:
        return num_ways(N-1) + num_ways(N-2)

# dynamic programming
# O(N)
def num_ways_bottom_up(N):
    if N == 0 or N == 1:
        return 1
    nums = []
    nums.append(1)
    nums.append(1)
    for i in range(2, N+1):
        nums.append(nums[i-1] + nums[i-2])
    return nums[N]

# dynamic programming with good space complexity
# O(N)
def num_ways_final(N):
    num1, num2 = 1, 1
    for _ in range(2, N+1):
        num1, num2 = num2, num1 + num2
    return num2

# generalized solution
# O(|X|^N)
def num_ways(N, X):
    if N < 0:
        return 0
    elif N == 0:
        return 1
    else:
        return sum(num_ways(N - x, X) for x in X)

# time complexity: O(|X| * N)
# space complexity: O(N)
def num_ways_final(N, X):
    cache = [0 for _ in range(N+1)]
    cache[0] = 1
    for i in range(1, N+1):
        cache[i] = sum(cache[i-x] for x in X if i - x >= 0)
    return cache[N]

print(num_ways_final(4, [1, 3, 5]))







