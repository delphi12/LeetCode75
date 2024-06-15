
#Given an array of Integers nums, if a number appears twice return false
#if it has distinct numbers, then return false

def containsDuplicate(arr):
    n = len(arr)
    s = set()
    for i in range(n):
        if arr[i] in s:
            return True
        else:
            s.add(arr[i])
    return False

arr=[1,2,3,4]
print(containsDuplicate(arr))