#given an array of integers nums and an integer target,
# return the indices of the two numbers that add up to the target.

#BruteForce Method
def solution(nums, target):
    n = len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if((nums[i]+nums[j])==target):
                print("Indices are ", i, j)
                break

#Optimized solution
def sol(nums, target):
    map ={}
    for i in range(0,len(nums)):
        diff = abs(nums[i]-target)
        if diff in map:
            print("Indices are ", map[diff], i)
            break
        else:
            map[nums[i]] = i

nums=[2,7,11,15]
target = 9  #(output: 0,1)

#nums =[3,2,4]
#target = 6  #(output: 1,2)

#solution(nums, target)

sol(nums, target)