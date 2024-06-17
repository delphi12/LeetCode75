#Given an array of Integers nums, find the contiguous subarray (containing atleast one number) which has the largest product
#i/p:

#Little complex, like dp, we are  calculation min_subarray and max_array. the need for min value is [-1,-2,-3]
#if all the integers are negative, and only considering max_subarray [-1*-2] = 2, [2*-3] = -6, if we have min_subarray
# [-1*-2] = 2 (max), -2 (min), [2*-3] = -6(min) [-2*-3] =6(max)
# so it will better for edge cases, likewise if it is zero, rest the curr_max and curr_min=1

def max_product_subarray(arr):
    res = max(arr)
    curr_max, curr_min = 1,1
    for n in arr:
        if n==0:
            curr_max,curr_min=1,1
            continue
        temp = n * curr_max
        curr_max = max(curr_max * n, curr_min * n, n) #why n? [-1,8], then max=-8, min=-8, n=8 (n is larger by itself)
        curr_min = min(temp, curr_min * n, n) #[-1,-8] min would be -8
        res = max(res, curr_max, curr_min)
    return res

arr= [2,3,-2,4]
print(max_product_subarray(arr))
