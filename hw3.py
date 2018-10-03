
"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""
def matrix_multiply(arr0, arr1):
    
    if (len(arr0[0]) != len(arr1)):
        return None
    resultArray = [[0 for row in range(len(arr1[0]))] for col in range(len(arr0))]
    for i in range(len(arr0)):
        for j in range(len(arr1[0])):
            for k in range(len(arr0[0])):
                resultArray[i][j] += arr0[i][k] * arr1[k][j]
    return resultArray

"""
nth_largest_element

Given an input list `arr`, and index `n`, return the nth largest element.
Avoid using built-in sorting methods.
"""
def nth_largest_element(arr, n):
    if len(arr) == 0 or arr == None or n == 0 or n > len(arr):
        return None
    sort = False
    while not sort:
        sort = True
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                sort = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr[n - 1]

"""
reverse_block

Given an input list `arr`, and a block size `n` > 0, reverse the list in blocks of n.

Example:
	Arguments:
		[1,2,3, 4,5,6, 7], 3
	Return:
		[3,2,1, 6,5,4, 7]
	(spacing added for emphasis)

"""
def reverse_block(arr, n):
    x = []
    if arr == None:
        return None
    if n > len(arr) or n == 0:
        return None
    if len(arr) == 0 or n == 1:
        return arr
    i = 0
    while i < len(arr):
        counter = 0
        subarr = []
        while i < len(arr) and counter < n:
            subarr.append(arr[i])
            i += 1
            counter += 1
        subarr.reverse()
        x += subarr
    return x

"""
subset_sum

Given an input list `arr`, and a number `target`, return whether or not any possible subset of the values in `arr` could sum to `target`.

Example 1:
	Arguments:
		[1,2,3,4,5,7], 13
		7 + 4 + 2 = 13
	Return:
		True

Example 2:
	Arguments:
		[1,2,-1,5,4,-196], 196
	Return:
		False
"""

def subset_sum(arr, target):
    if len(arr) == 0:
        return False
    else:
        if arr[0] == target:
            return True
        else:
            return subset_sum(arr[1:],(target - arr[0])) or subset_sum(arr[1:], target)

"""
spiral_matrix

Given an input 2-D array, return a list with the values obtained by following a clockwise spiral path, starting from [0][0], then proceeding to [0][n], [m][n], [m][0], then going inwards:

Example:
	Argument:
		[[a,b,c,d,e],
		 [f,g,h,i,j],
		 [k,l,m,n,o],
		 [p,q,r,s,t],
		 [u,v,w,x,y]]
	Return:
		[a,b,c,d,e, j,o,t,y, x,w,v,u, p,k,f, g,h,i, n,s, r,q, l, m]
"""
def spiral_matrix(arr):
    k = 0
    l = 0
    m = len(arr)
    n = len(arr[0])
    
    newArr = []
    while (k < m and l < n):
        for i in range(l, n):
            newArr.append(arr[k][i])
        
        k += 1
        
        for i in range(k, m):
            newArr.append(arr[i][n - 1])
        
        n -= 1
        
        if (k < m):
            for i in range(n - 1, l - 1, -1):
                newArr.append(arr[m - 1][i])
                
            m -= 1
        
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                newArr.append(arr[i][l])
                
            l += 1
    return newArr

