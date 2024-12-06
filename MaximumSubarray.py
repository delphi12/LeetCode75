#Given an integer array nums, find the contiguous subarray (containing atleast one number) which has the largest sum
# and return it's sum
#i/p: [-2,1,-3,4,-1,2,1,-5,4]
#o/p: 6
#explanation: [4,-1,2,1]

#Brute force: 0(n^3)
#If we use memory to store the sub-array computations it will reduce to 0(n^2)
#sliding window: 0(n) -> linear

def max_subarray(arr):
    n = len(arr)
    max_sum =arr[0]
    curr_sum=0
    for i in range(n):
        if curr_sum < 0:
            curr_sum =0
        curr_sum +=arr[i]
        max_sum = max(max_sum, curr_sum)
    print(max_sum)


#arr=[-2,1,-3,4,-1,2,1,-5,4]
#max_subarray(arr)

arr=[2,-8,3,-2,4,-10]
max_subarray(arr)