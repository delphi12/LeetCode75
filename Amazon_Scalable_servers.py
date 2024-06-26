"""AWS provides scalable systems. A set of n servers are used for horizontally scaling an application. The goal is to have the computational power of the servers in non-decreasing order. To do so, you can increase the computational power of each server in any contiguous segment by x. Choose the values of x such that after the computational powers are in non-decreasing order, the sum of the x values is minimum.
Example
There are n = 5 servers and their computational
power = [3,4,1,6,2].
Add 3 units to the subarray, (2, 4) and 4 units to the subarray (4, 4). The final arrangement of the
servers is: [3, 4, 4, 9, 9]. The answer is 3 + 4 = 7

sample Case 1: [3,2,1]
output: 2
Explanation: Add 1 unit to subarray (1,2) and 1 unit to subarray (2, 2).
The final arrangement of servers is [3,3,3].

Sample case 2: [3,5,2,3]
output: 3
Explanation: Add 3 units to subarray (2, 3). The final arrangement of servers is [3,5,5,6].

"""

def solution(arr):
    n = len(arr)
    power=0
    for i in range(n-1):
        arr[i+1] = arr[i+1]+power
        if arr[i] <= arr[i+1]:
            continue
        else:
            diff = arr[i]-arr[i+1]
            power = power+diff
            arr[i+1] = arr[i+1] + diff
    print(arr)
    return power

#arr = [3,4,1,6,2]
#arr = [3,2,1]
arr = [3,5,2,3]
print(solution(arr))
