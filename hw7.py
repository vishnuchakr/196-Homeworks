'''
Dear Students,

We release HW7 for *extra credit!*
Please see Piazza for more details.

REMINDER: cheating on this homework will result in a FAIR case!

Best Wishes!
'''

'''
max_nesting

Given an iterable (could be a list, tuple, or set),
return the deepest number of levels of nesting of the iterable.

If the sequence contains itself, directly or otherwise,
return -1 * the fewest levels of nesting before the sequence
(or any part of itself) is encountered.

Example 1:
	Argument:
		[[3, 4], [2, 3]]
		This is a 2D list.
	Return:
		2

Example 2:
	Argument:
		[[[3, 4], 3], 4]
		There are three levels of nesting.
	Return:
		3

For examples 3 and 4, suppose we evaluate the following list:
a = [[3], [2, 3]]
a[0][0] = a

Example 3:
	Argument:
		a
		Since a[0][0] = a, a is nested 2 levels deep inside itself.
	Return:
		-2

Example 4:
	Argument:
		[[a]]
		Now, a is still nested 2 levels deep inside itself,
		but there are two more outer layers of nesting.
	Return:
		-4
'''
def max_nesting(obj):
	pass


'''
almost_product

Given a list of integers, return a list of integers 'output'
wherein the value of output[i] is the product of all the
numbers in the input array except for input[i].

The input list always contains at least two elements.

You will lose points if your solution uses division.
Your solution should run in O(n) time.
Your solution should not allocate any space other than the output list.

Example 1:
	Argument:
		[2,3,4,5]
		Returned list should be [3*4*5, 2*4*5, 2*3*4]
	Return:
		[60, 40, 30, 24]

Example 2:
	Argument:
		[3,6,9,-3,2,-2]
	Return:
		[648, 324, 216, -648, 972, -972]
'''
def almost_product(arr):
    toReturn = []
    for i in range(0, len(arr)):
        toAppend = 1
        for j in range(0, len(arr)):
            if arr[j] != arr[i]:
                toAppend *= arr[j]
        toReturn.append(toAppend)   
    return toReturn


'''
staircase_ways

One day, Alice's power went out.
Because Alice is in 374 and also taking number theory classes,
she decided to count how many distinct ways she can climb up her staircase,
from the bottom to the last stair.
Alice can sometimes ascend more than one step because she has long legs.

Given the length of her staircase `stairs`,
and the maximum number of steps she may ascend per move `skip`,
determine the number of distinct ways she may climb up the staircase.
Note that Alice must start at the bottom, i.e. the 0th step,
and finish exactly at the Nth step where N is the number of stairs.

HINT: this is a harder version of a midterm coding question.

Ungraded food for thought: Think about the case where Alice has a limit
on the number of times she can ascend more than one step at a time.
(This makes the problem *much* more difficult.)

Example 1:
	Arguments:
		3, 1
		There is only one way for Alice to ascend at most one step at a time.
		BOTTOM -> 1 -> 2 -> 3
	Return:
		1

Example 2:
	Arguments:
		3, 2
		There are three ways to ascend at most two steps at a time:
		BOTTOM -> 1 -> 2 -> 3
		BOTTOM -> 1 -> 3
		BOTTOM -> 2 -> 3
	Return:
		3

Example 3:
	Arguments:
		5, 3
		There are 13 ways to go about this:
		BOTTOM -> 1 -> 2 -> 3 -> 4 -> 5
		BOTTOM -> 1 -> 2 -> 3 -> 5
		BOTTOM -> 1 -> 2 -> 4 -> 5
		BOTTOM -> 1 -> 3 -> 4 -> 5
		...
		BOTTOM -> 3 -> 5
	Return:
		13
'''
def staircase_ways(stairs, skip):
    skips = []
    for i in range(1, skip + 1):
        skips.append(i)
    
    def ways(stairs):
        if stairs == 0:
            return 1
        numWays = 0
        for i in skips:
            if stairs - i >= 0:
                numWays += ways(stairs - i)
        return numWays
    
    return ways(stairs)

'''
longest_increasing_subsequence

Given a list of integers, return the *length* of the longest increasing subsequence.

The definition of subsequence is the same as usual, i.e.
any (possibly non-contiguous) ordered subset of the array.

For example array [3, 2, 6, 4, 5, 8]:
	[2, 3, 4, 5] is not a subsequence.
	[3, 6, 4] is a non-increasing subsequence.
	[2, 5] is a increasing subsequence.
	[2, 4, 5, 8] is the longest increasing subsequence.

All values in the input list are unique.
'''
def longest_increasing_subsequence(arr):
    smallest = arr[0]
    sequence = [arr[0]]
    for i in range(1, len(arr) - 1):
        if arr[i] < smallest:
            smallest = arr[i]
            sequence = []
        if arr[i] < arr[i + 1]:
            sequence.append(arr[i])
    if arr[-1] > arr[-2]:
        sequence.append(arr[-1])
    return len(sequence)

'''
edit_distance

Given two strings, a and b, return the edit distance between the two strings.
An edit to a string consists of adding, removing, or changing a single character.
(This is a colloquial restatement of Levenshtein distance.)

Ungraded food for thought: your method should work on lists
with arbitrary elements, as well.

Example:
	Arguments:
		'kitten', 'sitting'
		To transform kitten into sitting, we can:
		k -> s
		e -> i
		add a g at the end
	Return:
		3
'''
def edit_distance(a, b):
    pass


'''
maximal_sum_subarray

Given a list of integers, return a list with two values [a,b]
such that arr[a:a+b] is the subarray with the largest sum.
For this problem, the subarray must be non-empty, i.e. b != 0.

If multiple such subarrays exist, return any one valid answer.

Ungraded food for thought: what about if we took the maximal product instead?
(This is a 374 DP problem.)
'''
def maximal_sum_subarray(arr):
    pass


'''
longest_palindromic_substring

Given a string, return the a list with list with two values [a,b]
such that the_string[a:a+b] is the longest palindromic substring in the_string.

The answer is guaranteed to be unique,
i.e. we will not test tiebreaking behavior.

Ungraded food for thought: your method should work on lists
with arbitrary elements, as well. (This is starting to feel familiar!)
'''
def longest_palindromic_substring(the_string):
	pass


'''
Thank you for playing.
- Andrew
'''


print(maximal_sum_subarray([1, 3, -5, 6, -1, 18, -70]))
